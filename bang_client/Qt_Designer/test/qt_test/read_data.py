import sys
import ui_read_data

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QListWidget, QListWidgetItem, QLabel

import write_data


class read_data_class(QtWidgets.QWidget, ui_read_data.Ui_MainWindow):
    def __init__(self, MainWindow, user, password):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(MainWindow)

        self.textEditUser.setText(user)
        self.textEditPassword.setText(password)

        self.BackButton.clicked.connect(lambda: self.back(MainWindow))

        self.label_1.setAcceptDrops(True)

    def back(self, MainWindow):
        wd = write_data.write_data_class(MainWindow)

    def mousePressEvent(self, event):
        #self.BackButton.mousePressEvent(self, event)
        if event.button() == Qt.LeftButton:
            print('press')