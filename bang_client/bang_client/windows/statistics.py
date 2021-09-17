from PyQt5.QtGui import QPixmap

import windows.base_windows.statistics

import windows.main_menu
import game_process

import sys
from PyQt5 import QtWidgets

class statistics_class(QtWidgets.QWidget, windows.base_windows.statistics.Ui_StatisticWindow):
    imageLabelBackDirectory = 'images/icons/arrows/006-arrow.png'

    def __init__(self, mainWindow):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)

        self.loadLabels()
        self.loadStatistics()

        self.labelBack.clicked.connect(lambda: self.labelBackClicked(mainWindow))

    def loadLabels(self):
        buttonBackImage = QPixmap(self.imageLabelBackDirectory)
        buttonBackImage = buttonBackImage.scaled(45, 45)
        self.labelBack.setPixmap(buttonBackImage)

    def loadStatistics(self):
        gp = game_process.game_process_class()
        gp.loadStatistics()

        self.label_11.setText(gp.statistics[0])
        self.label_12.setText(gp.statistics[1])
        self.label_13.setText(gp.statistics[2])
        self.label_14.setText(gp.statistics[3])
        self.label_15.setText(gp.statistics[4])
        self.label_16.setText(gp.statistics[5])
        self.label_17.setText(gp.statistics[6])
        self.label_18.setText(gp.statistics[7])
        self.label_19.setText(gp.statistics[8])

    def labelBackClicked(self, mainWindow):
        main_menu = windows.main_menu.main_menu_class(mainWindow)