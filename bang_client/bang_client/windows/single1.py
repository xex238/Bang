from PyQt5.QtGui import QPixmap

import windows.base_windows.single1

# import windows.main_menu
import windows.loading
import windows.get_random_role

import sys
from PyQt5 import QtWidgets

class single1_class(QtWidgets.QWidget, windows.base_windows.single1.Ui_MainWindowSingle1):
    imageLabelBackFile = 'images/icons/arrows/006-arrow.png'
    imageLabelNextFile = 'images/icons/arrows/005-arrow.png'

    count_of_players = 4
    level = 'Лёгкий'

    def __init__(self, mainWindow):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)

        self.loadLabels()

        self.labelPlayersInfo.setText(str(self.count_of_players))
        self.labelLevelInfo.setText(str(self.level))

        self.labelBack.clicked.connect(lambda: self.labelBackClicked(mainWindow))
        self.labelNext.clicked.connect(lambda: self.labelNextClicked(mainWindow))
        self.buttonPlayersMinus.clicked.connect(lambda: self.buttonPlayersMinusClicked())
        self.buttonPlayersPlus.clicked.connect(lambda: self.buttonPlayersPlusClicked())
        self.buttonLevelMinus.clicked.connect(lambda: self.buttonLevelMinusClicked())
        self.buttonLevelPlus.clicked.connect(lambda: self.buttonLevelPlusClicked())

    def loadLabels(self):
        buttonBackImage = QPixmap(self.imageLabelBackFile)
        buttonBackImage = buttonBackImage.scaled(45, 45)
        self.labelBack.setPixmap(buttonBackImage)

        buttonNextImage = QPixmap(self.imageLabelNextFile)
        buttonNextImage = buttonNextImage.scaled(45, 45)
        self.labelNext.setPixmap(buttonNextImage)

    def labelBackClicked(self, mainWindow):
        # main_menu = windows.main_menu.main_menu_class(mainWindow)
        loading = windows.loading.loading_class(mainWindow)

    def labelNextClicked(self, mainWindow):
        get_random_role = windows.get_random_role.get_random_role_class(mainWindow)

    def buttonPlayersMinusClicked(self):
        if(int(self.labelPlayersInfo.text()) > 4):
            self.labelPlayersInfo.setText(str(int(self.labelPlayersInfo.text()) - 1))
            self.count_of_players = self.count_of_players - 1

    def buttonPlayersPlusClicked(self):
        if(int(self.labelPlayersInfo.text()) < 7):
            self.labelPlayersInfo.setText(str(int(self.labelPlayersInfo.text()) + 1))
            self.count_of_players = self.count_of_players + 1

    def buttonLevelMinusClicked(self):
        if(str(self.labelLevelInfo.text()) == 'Тяжёлый'):
            self.labelLevelInfo.setText('Средний')
        elif(str(self.labelLevelInfo.text()) == 'Средний'):
            self.labelLevelInfo.setText('Лёгкий')

    def buttonLevelPlusClicked(self):
        if(str(self.labelLevelInfo.text()) == 'Лёгкий'):
            self.labelLevelInfo.setText('Средний')
        elif(str(self.labelLevelInfo.text()) == 'Средний'):
            self.labelLevelInfo.setText('Тяжёлый')