import windows.base_windows.game

import sys
from PyQt5 import QtWidgets

class game_class(QtWidgets.QWidget, windows.base_windows.game.Ui_GameWindow):
    def __init__(self, mainWindow):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)