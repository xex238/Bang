#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import windows.main_menu
import game_process

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QPushButton, QWidget, QLineEdit, QApplication)

if __name__ == '__main__':
    gp = game_process.game_process_class()

    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    mainMenu = windows.main_menu.main_menu_class(MainWindow)

    if(gp.login != ""):
        mainMenu.label_guest.setText(str(gp.login))

    MainWindow.show()
    sys.exit(app.exec_())