# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'authorization.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AuthorizationWindow(object):
    def setupUi(self, AuthorizationWindow):
        AuthorizationWindow.setObjectName("AuthorizationWindow")
        AuthorizationWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(AuthorizationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(287, 184, 450, 400))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(5)
        self.frame.setMidLineWidth(5)
        self.frame.setObjectName("frame")
        self.labelUsername = QtWidgets.QLabel(self.centralwidget)
        self.labelUsername.setGeometry(QtCore.QRect(310, 260, 106, 21))
        self.labelUsername.setObjectName("labelUsername")
        self.plainTextEditUsername = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditUsername.setGeometry(QtCore.QRect(310, 292, 404, 27))
        self.plainTextEditUsername.setObjectName("plainTextEditUsername")
        self.labelPassword = QtWidgets.QLabel(self.centralwidget)
        self.labelPassword.setGeometry(QtCore.QRect(310, 335, 103, 21))
        self.labelPassword.setObjectName("labelPassword")
        self.plainTextEditPassword = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditPassword.setGeometry(QtCore.QRect(310, 367, 404, 27))
        self.plainTextEditPassword.setObjectName("plainTextEditPassword")
        self.buttonBack = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBack.setGeometry(QtCore.QRect(310, 520, 67, 27))
        self.buttonBack.setObjectName("buttonBack")
        self.buttonNext = QtWidgets.QPushButton(self.centralwidget)
        self.buttonNext.setGeometry(QtCore.QRect(649, 529, 67, 27))
        self.buttonNext.setObjectName("buttonNext")
        AuthorizationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AuthorizationWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        AuthorizationWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AuthorizationWindow)
        self.statusbar.setObjectName("statusbar")
        AuthorizationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AuthorizationWindow)
        QtCore.QMetaObject.connectSlotsByName(AuthorizationWindow)

    def retranslateUi(self, AuthorizationWindow):
        _translate = QtCore.QCoreApplication.translate
        AuthorizationWindow.setWindowTitle(_translate("AuthorizationWindow", "???????????? ????????. ????????"))
        self.labelUsername.setText(_translate("AuthorizationWindow", "?????????????? ??????????"))
        self.labelPassword.setText(_translate("AuthorizationWindow", "?????????????? ????????????"))
        self.buttonBack.setText(_translate("AuthorizationWindow", "??????????"))
        self.buttonNext.setText(_translate("AuthorizationWindow", "????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AuthorizationWindow = QtWidgets.QMainWindow()
    ui = Ui_AuthorizationWindow()
    ui.setupUi(AuthorizationWindow)
    AuthorizationWindow.show()
    sys.exit(app.exec_())
