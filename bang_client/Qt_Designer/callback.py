# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'callback.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CallbackWindow(object):
    def setupUi(self, CallbackWindow):
        CallbackWindow.setObjectName("CallbackWindow")
        CallbackWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(CallbackWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEditMessage = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditMessage.setGeometry(QtCore.QRect(302, 221, 420, 305))
        self.textEditMessage.setObjectName("textEditMessage")
        self.buttonBack = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBack.setGeometry(QtCore.QRect(302, 529, 100, 27))
        self.buttonBack.setObjectName("buttonBack")
        self.buttonSend = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSend.setGeometry(QtCore.QRect(622, 529, 100, 27))
        self.buttonSend.setObjectName("buttonSend")
        self.labelInfo = QtWidgets.QLabel(self.centralwidget)
        self.labelInfo.setGeometry(QtCore.QRect(412, 100, 200, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelInfo.sizePolicy().hasHeightForWidth())
        self.labelInfo.setSizePolicy(sizePolicy)
        self.labelInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInfo.setObjectName("labelInfo")
        self.labelMainInfo = QtWidgets.QLabel(self.centralwidget)
        self.labelMainInfo.setGeometry(QtCore.QRect(302, 130, 200, 25))
        self.labelMainInfo.setObjectName("labelMainInfo")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(302, 160, 420, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(302, 195, 200, 25))
        self.label.setObjectName("label")
        CallbackWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CallbackWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        CallbackWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CallbackWindow)
        self.statusbar.setObjectName("statusbar")
        CallbackWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CallbackWindow)
        QtCore.QMetaObject.connectSlotsByName(CallbackWindow)

    def retranslateUi(self, CallbackWindow):
        _translate = QtCore.QCoreApplication.translate
        CallbackWindow.setWindowTitle(_translate("CallbackWindow", "???????????????? ??????????"))
        self.buttonBack.setText(_translate("CallbackWindow", "??????????"))
        self.buttonSend.setText(_translate("CallbackWindow", "??????????????????"))
        self.labelInfo.setText(_translate("CallbackWindow", "???????????????? ??????????"))
        self.labelMainInfo.setText(_translate("CallbackWindow", "?????????????? ???????? ??????????:"))
        self.label.setText(_translate("CallbackWindow", "?????????????? ???????? ??????????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CallbackWindow = QtWidgets.QMainWindow()
    ui = Ui_CallbackWindow()
    ui.setupUi(CallbackWindow)
    CallbackWindow.show()
    sys.exit(app.exec_())
