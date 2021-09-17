import windows.base_windows.choice_character

import sys
from PyQt5 import QtWidgets

class choice_character_class(QtWidgets.QWidget, windows.base_windows.choice_character.Ui_MainWindowChoiceCharacter):
    def __init__(self, mainWindow):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)