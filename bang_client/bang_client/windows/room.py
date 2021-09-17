import windows.base_windows.room

import sys
from PyQt5 import QtWidgets

class room_class(QtWidgets.QWidget, windows.base_windows.room.Ui_WaitingPlayersWindow):
    def __init__(self, mainWindow):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)