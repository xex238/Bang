from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets

import windows.base_windows.rules
import windows.banglopedia_menu

import sys
import os
from glob import glob

class rules_class(QtWidgets.QWidget, windows.base_windows.rules.Ui_RulesWindow):
    labelBackFile = 'images/icons/arrows/006-arrow.png'
    labelBackPageFile = 'images/icons/arrows/002-arrow.png'
    labelNextPageFile = 'images/icons/arrows/0021-arrow.png'

    directory = 'images/rules'
    rule_images = []
    images_counter = 0

    def __init__(self, mainWindow):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)

        self.loadRules()
        self.loadLabels()

        self.labelBack.clicked.connect(lambda: self.labelBackClicked(mainWindow))
        self.labelBackPage.clicked.connect(lambda: self.labelBackPageClicked())
        self.labelNextPage.clicked.connect(lambda: self.labelNextPageClicked())

    def loadRules(self):
        if(len(self.rule_images) == 0):
            images = list(glob(os.path.join(self.directory, '*.jpg')))

            for i in range(len(images)):
                self.rule_images.append(QPixmap(images[i]))
        self.rule_images[self.images_counter] = self.rule_images[self.images_counter].scaled(480, 640)

        self.labelRules.setPixmap(self.rule_images[self.images_counter])

    def loadLabels(self):
        labelBackImage = QPixmap(self.labelBackFile)
        labelBackImage = labelBackImage.scaled(45, 45)
        self.labelBack.setPixmap(labelBackImage)

        labelBackPageImage = QPixmap(self.labelBackPageFile)
        labelBackPageImage = labelBackPageImage.scaled(45, 45)
        self.labelBackPage.setPixmap(labelBackPageImage)

        labelNextPageImage = QPixmap(self.labelNextPageFile)
        labelNextPageImage = labelNextPageImage.scaled(45, 45)
        self.labelNextPage.setPixmap(labelNextPageImage)

    def labelBackClicked(self, mainWindow):
        banglopedia_menu = windows.banglopedia_menu.banglopedia_menu_class(mainWindow)

    def labelBackPageClicked(self):
        if(self.images_counter > 0):
            self.images_counter = self.images_counter - 1
            self.rule_images[self.images_counter] = self.rule_images[self.images_counter].scaled(480, 640)
            self.labelRules.setPixmap(self.rule_images[self.images_counter])

    def labelNextPageClicked(self):
        if(self.images_counter < len(self.rule_images) - 1):
            self.images_counter = self.images_counter + 1
            self.rule_images[self.images_counter] = self.rule_images[self.images_counter].scaled(480, 640)
            self.labelRules.setPixmap(self.rule_images[self.images_counter])