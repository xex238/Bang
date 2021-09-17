# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_single_mode = QtWidgets.QPushButton(self.centralwidget)
        self.button_single_mode.setGeometry(QtCore.QRect(430, 252, 150, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_single_mode.sizePolicy().hasHeightForWidth())
        self.button_single_mode.setSizePolicy(sizePolicy)
        self.button_single_mode.setObjectName("button_single_mode")
        self.button_multi_mode = QtWidgets.QPushButton(self.centralwidget)
        self.button_multi_mode.setGeometry(QtCore.QRect(430, 292, 150, 25))
        self.button_multi_mode.setObjectName("button_multi_mode")
        self.label_guest = QtWidgets.QLabel(self.centralwidget)
        self.label_guest.setGeometry(QtCore.QRect(568, 215, 33, 21))
        self.label_guest.setAlignment(QtCore.Qt.AlignCenter)
        self.label_guest.setObjectName("label_guest")
        self.button_banglopedia = QtWidgets.QPushButton(self.centralwidget)
        self.button_banglopedia.setGeometry(QtCore.QRect(430, 332, 150, 25))
        self.button_banglopedia.setObjectName("button_banglopedia")
        self.button_settings = QtWidgets.QPushButton(self.centralwidget)
        self.button_settings.setGeometry(QtCore.QRect(430, 372, 150, 25))
        self.button_settings.setObjectName("button_settings")
        self.button_statistics = QtWidgets.QPushButton(self.centralwidget)
        self.button_statistics.setGeometry(QtCore.QRect(430, 412, 150, 25))
        self.button_statistics.setObjectName("button_statistics")
        self.button_callback = QtWidgets.QPushButton(self.centralwidget)
        self.button_callback.setGeometry(QtCore.QRect(430, 452, 150, 25))
        self.button_callback.setObjectName("button_callback")
        self.button_exit = QtWidgets.QPushButton(self.centralwidget)
        self.button_exit.setGeometry(QtCore.QRect(430, 492, 150, 25))
        self.button_exit.setObjectName("button_exit")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(392, 197, 240, 355))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(5)
        self.frame.setMidLineWidth(5)
        self.frame.setObjectName("frame")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главное меню"))
        self.button_single_mode.setText(_translate("MainWindow", "Одиночная игра"))
        self.button_multi_mode.setText(_translate("MainWindow", "Онлайн игра"))
        self.label_guest.setText(_translate("MainWindow", "Гость"))
        self.button_banglopedia.setText(_translate("MainWindow", "Бэнглопедия"))
        self.button_settings.setText(_translate("MainWindow", "Настройки"))
        self.button_statistics.setText(_translate("MainWindow", "Игровая статистика"))
        self.button_callback.setText(_translate("MainWindow", "Обратная связь"))
        self.button_exit.setText(_translate("MainWindow", "Выход"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
