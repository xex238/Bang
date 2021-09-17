# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'banglopedia_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BanglopediaWindow(object):
    def setupUi(self, BanglopediaWindow):
        BanglopediaWindow.setObjectName("BanglopediaWindow")
        BanglopediaWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(BanglopediaWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(399, 256, 225, 255))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(5)
        self.frame.setMidLineWidth(5)
        self.frame.setObjectName("frame")
        self.buttonHowToPlay = QtWidgets.QPushButton(self.centralwidget)
        self.buttonHowToPlay.setGeometry(QtCore.QRect(441, 280, 141, 27))
        self.buttonHowToPlay.setObjectName("buttonHowToPlay")
        self.buttonRolesCards = QtWidgets.QPushButton(self.centralwidget)
        self.buttonRolesCards.setGeometry(QtCore.QRect(441, 325, 141, 27))
        self.buttonRolesCards.setObjectName("buttonRolesCards")
        self.buttonCharactersCards = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCharactersCards.setGeometry(QtCore.QRect(441, 370, 141, 27))
        self.buttonCharactersCards.setObjectName("buttonCharactersCards")
        self.buttonGameCards = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGameCards.setGeometry(QtCore.QRect(441, 415, 141, 27))
        self.buttonGameCards.setObjectName("buttonGameCards")
        self.buttonMainMenu = QtWidgets.QPushButton(self.centralwidget)
        self.buttonMainMenu.setGeometry(QtCore.QRect(441, 460, 141, 27))
        self.buttonMainMenu.setObjectName("buttonMainMenu")
        BanglopediaWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BanglopediaWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        BanglopediaWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BanglopediaWindow)
        self.statusbar.setObjectName("statusbar")
        BanglopediaWindow.setStatusBar(self.statusbar)

        self.retranslateUi(BanglopediaWindow)
        QtCore.QMetaObject.connectSlotsByName(BanglopediaWindow)

    def retranslateUi(self, BanglopediaWindow):
        _translate = QtCore.QCoreApplication.translate
        BanglopediaWindow.setWindowTitle(_translate("BanglopediaWindow", "Бэнглопедия"))
        self.buttonHowToPlay.setText(_translate("BanglopediaWindow", "Как играть?"))
        self.buttonRolesCards.setText(_translate("BanglopediaWindow", "Карты ролей"))
        self.buttonCharactersCards.setText(_translate("BanglopediaWindow", "Карты персонажей"))
        self.buttonGameCards.setText(_translate("BanglopediaWindow", "Игровые карты"))
        self.buttonMainMenu.setText(_translate("BanglopediaWindow", "В главное меню"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BanglopediaWindow = QtWidgets.QMainWindow()
    ui = Ui_BanglopediaWindow()
    ui.setupUi(BanglopediaWindow)
    BanglopediaWindow.show()
    sys.exit(app.exec_())
