import windows.base_windows.authorization

import sys
from PyQt5 import QtWidgets

class authorization_class(QtWidgets.QWidget, windows.base_windows.authorization.Ui_AuthorizationWindow):
    def __init__(self, mainWindow):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)