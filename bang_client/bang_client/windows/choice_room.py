import windows.base_windows.choice_room

import windows.main_menu

import sys
from PyQt5 import QtWidgets

class choice_room_class(QtWidgets.QWidget, windows.base_windows.choice_room.Ui_ChoiceRoomWindow):
    def __init__(self, mainWindow):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)

        self.buttonBack.clicked.connect(lambda: self.buttonBackClicked(mainWindow))

    def buttonBackClicked(self, mainWindow):
        main_menu = windows.main_menu.main_menu_class(mainWindow)

    # def buttonCreateRoomClicked(self, mainWindow):