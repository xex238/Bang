import windows.base_windows.loading

import windows.main_menu
# import windows.get_random_role
import windows.single1

import sys
from PyQt5 import QtWidgets

class loading_class(QtWidgets.QWidget, windows.base_windows.loading.Ui_MainWindow):
    def __init__(self, mainWindow):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)

        self.buttonBack.clicked.connect(lambda: self.buttonBackClicked(mainWindow))
        self.buttonNext.clicked.connect(lambda: self.buttonNewGameClicked(mainWindow))

    def buttonBackClicked(self, mainWindow):
        main_menu = windows.main_menu.main_menu_class(mainWindow)

    def buttonNewGameClicked(self, mainWindow):
        # get_random_role = windows.get_random_role.get_random_role_class(mainWindow)
        single1 = windows.single1.single1_class(mainWindow)