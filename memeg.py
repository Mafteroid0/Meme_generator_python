# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'memeg.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(25, 25, 27);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.meme = QtWidgets.QLabel(self.centralwidget)
        self.meme.setGeometry(QtCore.QRect(310, 130, 426, 240))
        self.meme.setText("")
        self.meme.setPixmap(QtGui.QPixmap("../../../../../Program Files (x86)/Qt Designer/_91408619_55df76d5-2245-41c1-8031-07a4da3f313f.jpg"))
        self.meme.setScaledContents(False)
        self.meme.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 181, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(69, 70, 72);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 10pt \"Fulbo\";")
        self.lineEdit.setObjectName("lineEdit")
        self.list_of_memes = QtWidgets.QComboBox(self.centralwidget)
        self.list_of_memes.setGeometry(QtCore.QRect(20, 120, 191, 41))
        self.list_of_memes.setStyleSheet("background-color: rgb(69, 70, 72);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 10pt \"Fulbo\";")
        self.list_of_memes.setEditable(False)
        self.list_of_memes.setObjectName("comboBox")
        self.list_of_memes.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 450, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Fulbo")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setStyleSheet("background-color: rgb(69, 70, 72);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 10pt \"Fulbo\";\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(580, 510, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Fulbo")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.save.setFont(font)
        self.save.setStyleSheet("background-color: rgb(69, 70, 72);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 10pt \"Fulbo\";")
        self.save.setObjectName("save")
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(220, 120, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Fulbo")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.plus.setFont(font)
        self.plus.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.plus.setStyleSheet("background-color: rgb(69, 70, 72);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 10pt \"Fulbo\";\n"
"")
        self.plus.setObjectName("plus")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setText(_translate("MainWindow", "?????????????? ?????????? ?????? ????????"))
        self.list_of_memes.setItemText(0, _translate("MainWindow", "?????????????????? ????????...", "12"))
        self.pushButton.setText(_translate("MainWindow", "?????????????? ??????"))
        self.save.setText(_translate("MainWindow", "??????????????????.."))
        self.plus.setText(_translate("MainWindow", "+"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
