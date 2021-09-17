import windows.base_windows.registration

import sys
from PyQt5 import QtWidgets

class registration_class(QtWidgets.QWidget, windows.base_windows.registration.Ui_RegistrationWindow):
    def __init__(self, mainWindow):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)