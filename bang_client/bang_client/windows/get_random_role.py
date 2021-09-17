from PyQt5.QtGui import QPixmap

import windows.base_windows.get_random_role

import windows.single1

import sys
from PyQt5 import QtWidgets

class get_random_role_class(QtWidgets.QWidget, windows.base_windows.get_random_role.Ui_MainWindowRandomRole):
    imageLabelBackFile = 'images/icons/arrows/006-arrow.png'
    imageLabelNextFile = 'images/icons/arrows/005-arrow.png'

    def __init__(self, mainWindow):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)

        self.loadLabels()

        self.labelBack.clicked.connect(lambda: self.labelBackClicked(mainWindow))

    def loadLabels(self):
        buttonBackImage = QPixmap(self.imageLabelBackFile)
        buttonBackImage = buttonBackImage.scaled(45, 45)
        self.labelBack.setPixmap(buttonBackImage)

        buttonNextImage = QPixmap(self.imageLabelNextFile)
        buttonNextImage = buttonNextImage.scaled(45, 45)
        self.labelNext.setPixmap(buttonNextImage)

    def labelBackClicked(self, mainWindow):
        single1 = windows.single1.single1_class(mainWindow)