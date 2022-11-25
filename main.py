import sys
import io
from PIL import Image, ImageDraw, ImageFont
from PIL.ImageQt import ImageQt
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtCore import QBuffer
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QDialog
import sqlite3
from memeg import Ui_MainWindow
from form import Ui_MainWindow1


class MyPillow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyPillow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Генератор мемов")
        self.setWindowIcon(QtGui.QIcon('pepe.ico'))

        self.create_combobox()
        self.filename = "pepe.jpg"
        self.curr_image = Image.open(self.filename)
        self.qt_curr_img = ImageQt(self.curr_image)
        self.pixmap = QPixmap()
        self.pixmap.loadFromData(self.result_que[1][2], "jpg")

        self.pixmap_resized = self.pixmap.scaled(426, 240, QtCore.Qt.KeepAspectRatio)
        self.meme.setPixmap(self.pixmap_resized)

        self.img = QImage(self.filename)

        self.buffer = QBuffer()
        self.buffer.open(QBuffer.ReadWrite)
        self.img.save(self.buffer, "jpg")
        self.curr_image = Image.open(io.BytesIO(self.buffer.data()))

        self.qt_curr_img = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.qt_curr_img)
        self.meme.setPixmap(self.pixmap.scaled(
            426, 240, QtCore.Qt.KeepAspectRatio))

        self.list_of_memes.activated.connect(self.testc)
        self.list_of_memes.setCurrentIndex(2)
        self.pushButton.clicked.connect(self.memed)
        self.save.clicked.connect(self.saved)
        self.plus.clicked.connect(self.plussed)


    def memed(self):
        #self.img = QImage(self.filename)
        self.img = QImage(self.pixmap_resized)
        self.buffer = QBuffer()
        self.buffer.open(QBuffer.ReadWrite)
        self.img.save(self.buffer, "jpg")
        self.xim, self.yim = Image.open(io.BytesIO(self.buffer.data())).size
        self.curr_image = Image.open(io.BytesIO(self.buffer.data()))

        self.draw_text = ImageDraw.Draw(self.curr_image)
        if len(self.lineEdit.text()) > 12:
            self.siz = round((self.xim - 40)/len(self.lineEdit.text())) * 2
        else:
            self.siz = 104
        self.font = ImageFont.truetype('impact.ttf', size=self.siz)
        self.draw_text.text((20, self.yim - self.siz - 20), self.lineEdit.text(), fill=(
            'white'), font=self.font, stroke_width=round(self.siz / 21), stroke_fill='black')

        self.qt_curr_img = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.qt_curr_img)
        self.meme.setPixmap(self.pixmap.scaled(
            426, 240, QtCore.Qt.KeepAspectRatio))

    def create_combobox(self):
        cursor = connection_db.cursor()
        self.result_que = cursor.execute(
            "SELECT * FROM lovely_images").fetchall()
        for i in range(len(self.result_que)):
            self.list_of_memes.addItem(self.result_que[i][1])

    def testc(self):

        if self.list_of_memes.currentIndex() == 0:
            self.filename = QFileDialog.getOpenFileName(
                self, 'Выберите картинку', '', 'Картинки (*.jpg)')[0]
            if self.filename == "":
                self.filename = "pepe.jpg"
            self.pixmap = QPixmap(self.filename)

        else:
            self.pixmap = QPixmap()
            self.pixmap.loadFromData(self.result_que[self.list_of_memes.currentIndex() - 1][2], "jpg")
        self.pixmap_resized = self.pixmap.scaled(426, 240, QtCore.Qt.KeepAspectRatio)
        self.meme.setPixmap(self.pixmap_resized)

    def saved(self):
        self.out = QFileDialog.getSaveFileName(
            self, 'Сохранение', 'Мем.jpg', 'Картинка (*.jpg)')[0]
        if self.out != "":
            self.curr_image.save(self.out)

    def plussed(self):
        ex1 = Dialog(parent=self)
        ex1.show()
        ex.hide()


class Dialog(QMainWindow, Ui_MainWindow1):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon('pepe.ico'))
        self.setupUi(self)
        self.show()
        self.setWindowTitle("Добавить изображение в список")
        self.pushButton.clicked.connect(self.open)
        self.ok.clicked.connect(self.okk)
        self.cancel.clicked.connect(self.back)

    def open(self):
        self.file = QFileDialog.getOpenFileName(
            self, 'Выберите картинку', '', 'Картинки (*.jpg)')[0]
        if self.file == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Внимание!")
            msg.setInformativeText('Вы не выбрали изображение')
            msg.setWindowTitle("Некорректно выбран файл")
            msg.exec_()

    def okk(self):
        cursor = connection_db.cursor()

        def convert_to_binary_data(filename):
            with open(filename, 'rb') as file:
                blob_data = file.read()
            return blob_data

        resume = convert_to_binary_data(self.file)
        blob_query = "INSERT INTO lovely_images(name, img) VALUES(?, ?)"
        imp = (self.login.text(), resume)
        cursor.execute(blob_query, imp)
        connection_db.commit()
        self.close()
        global ex
        ex.close()
        ex = MyPillow()
        ex.show()

    def back(self):
        self.close()
        ex.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    connection_db = sqlite3.connect('memes.db')
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec())
