import windows.base_windows.create_room

import sys
from PyQt5 import QtWidgets

class create_room_class(QtWidgets.QWidget, windows.base_windows.create_room.Ui_CreateRoomWindow):
    def __init__(self, mainWindow):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)