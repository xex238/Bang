import windows.base_windows.game_result

import sys
from PyQt5 import QtWidgets

class game_result_class(QtWidgets.QWidget, windows.base_windows.game_result.Ui_GameResultWindow):
    def __init__(self, mainWindow):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)