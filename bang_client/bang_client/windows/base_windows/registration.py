# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegistrationWindow(object):
    def setupUi(self, RegistrationWindow):
        RegistrationWindow.setObjectName("RegistrationWindow")
        RegistrationWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(RegistrationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(287, 184, 450, 400))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(5)
        self.frame.setMidLineWidth(5)
        self.frame.setObjectName("frame")
        self.labelUsername = QtWidgets.QLabel(self.centralwidget)
        self.labelUsername.setGeometry(QtCore.QRect(310, 260, 120, 21))
        self.labelUsername.setObjectName("labelUsername")
        self.plainTextEditLogin = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditLogin.setGeometry(QtCore.QRect(310, 292, 404, 27))
        self.plainTextEditLogin.setObjectName("plainTextEditLogin")
        self.labelPassword = QtWidgets.QLabel(self.centralwidget)
        self.labelPassword.setGeometry(QtCore.QRect(310, 335, 120, 21))
        self.labelPassword.setObjectName("labelPassword")
        self.plainTextEditPassword = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditPassword.setGeometry(QtCore.QRect(310, 367, 404, 27))
        self.plainTextEditPassword.setObjectName("plainTextEditPassword")
        self.labelRepeatPassword = QtWidgets.QLabel(self.centralwidget)
        self.labelRepeatPassword.setGeometry(QtCore.QRect(310, 410, 120, 21))
        self.labelRepeatPassword.setObjectName("labelRepeatPassword")
        self.plainTextEditRepeatPassword = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditRepeatPassword.setGeometry(QtCore.QRect(310, 442, 404, 27))
        self.plainTextEditRepeatPassword.setObjectName("plainTextEditRepeatPassword")
        self.buttonBack = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBack.setGeometry(QtCore.QRect(310, 520, 67, 27))
        self.buttonBack.setObjectName("buttonBack")
        self.buttonNext = QtWidgets.QPushButton(self.centralwidget)
        self.buttonNext.setGeometry(QtCore.QRect(649, 520, 67, 27))
        self.buttonNext.setObjectName("buttonNext")
        RegistrationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RegistrationWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        RegistrationWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RegistrationWindow)
        self.statusbar.setObjectName("statusbar")
        RegistrationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegistrationWindow)
        QtCore.QMetaObject.connectSlotsByName(RegistrationWindow)

    def retranslateUi(self, RegistrationWindow):
        _translate = QtCore.QCoreApplication.translate
        RegistrationWindow.setWindowTitle(_translate("RegistrationWindow", "Онлайн игра. Регистрация"))
        self.labelUsername.setText(_translate("RegistrationWindow", "Введите логин"))
        self.labelPassword.setText(_translate("RegistrationWindow", "Введите пароль"))
        self.labelRepeatPassword.setText(_translate("RegistrationWindow", "Повторите пароль"))
        self.buttonBack.setText(_translate("RegistrationWindow", "Назад"))
        self.buttonNext.setText(_translate("RegistrationWindow", "Далее"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegistrationWindow = QtWidgets.QMainWindow()
    ui = Ui_RegistrationWindow()
    ui.setupUi(RegistrationWindow)
    RegistrationWindow.show()
    sys.exit(app.exec_())