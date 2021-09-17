import windows.base_windows.online1

import windows.authorization
import windows.registration
import windows.main_menu

import sys
from PyQt5 import QtWidgets

class online1_class(QtWidgets.QWidget, windows.base_windows.online1.Ui_MainWindowOnline1):
    def __init__(self, mainWindow):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)

    def buttonAuthorizationClicked(self, mainWindow):
        authorization = windows.authorization.authorization_class(mainWindow)

    def buttonRegistrationClicked(self, mainWindow):
        registration = windows.registration.registration_class(mainWindow)

    def buttonBackClicked(self, mainWindow):
        main_menu = windows.main_menu.main_menu_class(mainWindow)