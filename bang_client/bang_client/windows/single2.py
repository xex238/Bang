import windows.base_windows.single2

import sys
from PyQt5 import QtWidgets

class single2_class(QtWidgets.QWidget, windows.base_windows.single2.Ui_MainWindowSingle2):
    def __init__(self, mainWindow):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)