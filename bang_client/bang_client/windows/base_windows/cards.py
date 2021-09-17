# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cards.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
from glob import glob
import sip

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QScrollArea

import clicked_label

class Ui_CardsWindow(object):
    directory_roles = 'images/cards/roles'
    directory_characters = 'images/cards/characters'
    directory_game_cards = 'images/cards/game_cards'

    roles_images = []
    characters_images = []
    game_cards_images = []

    roles_labels = []
    characters_labels = []
    game_cards_labels = []

    start_x = 35
    start_y = 35
    width_ = 150
    height_ = 200
    dx = 30
    dy = 30

    cards_in_row = 4

    def setupUi(self, CardsWindow):
        CardsWindow.setObjectName("CardsWindow")
        CardsWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(CardsWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.labelBack = QtWidgets.QLabel(self.centralwidget)
        self.labelBack = clicked_label.ClickedLabel(self.centralwidget)
        self.labelBack.setGeometry(QtCore.QRect(15, 15, 48, 48))
        self.labelBack.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBack.setObjectName("labelBack")
        self.tabWidgetCards = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidgetCards.setGeometry(QtCore.QRect(75, 75, 933, 737))
        self.tabWidgetCards.setObjectName("tabWidgetCards")
        self.tabRoles = QtWidgets.QWidget()
        self.tabRoles.setObjectName("tabRoles")

        # Новые объекты
        #
        self.scrollAreaRoles = QtWidgets.QScrollArea(self.tabRoles)
        self.scrollAreaRoles.setGeometry(QtCore.QRect(10, 10, 901, 601))
        self.scrollAreaRoles.setWidgetResizable(True)
        self.scrollAreaRoles.setObjectName("scrollAreaRoles")

        self.scrollAreaWidgetContentsRoles = QtWidgets.QWidget()
        self.scrollAreaWidgetContentsRoles.setGeometry(QtCore.QRect(0, 0, 882, 1024))
        self.scrollAreaWidgetContentsRoles.setObjectName("scrollAreaWidgetContentsRoles")

        self.gridLayoutRoles = QtWidgets.QGridLayout(self.scrollAreaWidgetContentsRoles)
        self.gridLayoutRoles.setObjectName("gridLayoutRoles")

        self.scrollAreaRoles.setWidget(self.scrollAreaWidgetContentsRoles)
        #

        self.tabWidgetCards.addTab(self.tabRoles, "")

        self.tabCharacters = QtWidgets.QWidget()
        self.tabCharacters.setObjectName("tabCharacters")

        # Новые объекты
        #
        self.scrollAreaCharacters = QtWidgets.QScrollArea(self.tabCharacters)
        self.scrollAreaCharacters.setGeometry(QtCore.QRect(10, 10, 901, 601))
        self.scrollAreaCharacters.setWidgetResizable(True)
        self.scrollAreaCharacters.setObjectName("scrollAreaCharacters")

        self.scrollAreaWidgetContentsCharacters = QtWidgets.QWidget()
        self.scrollAreaWidgetContentsCharacters.setGeometry(QtCore.QRect(0, 0, 882, 1024))
        self.scrollAreaWidgetContentsCharacters.setObjectName("scrollAreaWidgetContentsCharacters")

        self.gridLayoutCharacters = QtWidgets.QGridLayout(self.scrollAreaWidgetContentsCharacters)
        self.gridLayoutCharacters.setObjectName("gridLayoutCharacters")

        self.scrollAreaCharacters.setWidget(self.scrollAreaWidgetContentsCharacters)
        #

        self.tabWidgetCards.addTab(self.tabCharacters, "")

        self.tabGameCards = QtWidgets.QWidget()
        self.tabGameCards.setObjectName("tabGameCards")

        # Новые объекты
        #
        self.scrollAreaGameCards = QtWidgets.QScrollArea(self.tabGameCards)
        self.scrollAreaGameCards.setGeometry(QtCore.QRect(10, 10, 901, 601))
        self.scrollAreaGameCards.setWidgetResizable(True)
        self.scrollAreaGameCards.setObjectName("scrollAreaCharacters")

        self.scrollAreaWidgetContentsGameCards = QtWidgets.QWidget()
        self.scrollAreaWidgetContentsGameCards.setGeometry(QtCore.QRect(0, 0, 882, 1024))
        self.scrollAreaWidgetContentsGameCards.setObjectName("scrollAreaWidgetContentsCharacters")

        self.gridLayoutGameCards = QtWidgets.QGridLayout(self.scrollAreaWidgetContentsGameCards)
        self.gridLayoutGameCards.setObjectName("gridLayoutCharacters")

        self.scrollAreaGameCards.setWidget(self.scrollAreaWidgetContentsGameCards)
        #

        self.tabWidgetCards.addTab(self.tabGameCards, "")
        CardsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CardsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        CardsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CardsWindow)
        self.statusbar.setObjectName("statusbar")
        CardsWindow.setStatusBar(self.statusbar)

        self.loadImages(CardsWindow)

        self.retranslateUi(CardsWindow)
        QtCore.QMetaObject.connectSlotsByName(CardsWindow)

        #if(len(self.roles_images) == 0):
        self.setImages()

    def retranslateUi(self, CardsWindow):
        _translate = QtCore.QCoreApplication.translate
        CardsWindow.setWindowTitle(_translate("CardsWindow", "Карты"))
        self.labelBack.setText(_translate("CardsWindow", "<"))
        self.tabWidgetCards.setTabText(self.tabWidgetCards.indexOf(self.tabRoles), _translate("CardsWindow", "Роли"))
        self.tabWidgetCards.setTabText(self.tabWidgetCards.indexOf(self.tabCharacters), _translate("CardsWindow", "Персонажи"))
        self.tabWidgetCards.setTabText(self.tabWidgetCards.indexOf(self.tabGameCards), _translate("CardsWindow", "Игровые карты"))

    def loadImages(self, mainWindow):
        #if(len(self.roles_images) == 0):
        self.loadRolesImages()
        self.loadCharactersImages()
        self.loadGameCards()

        #self.setImages(mainWindow)

    def loadRolesImages(self):
        images = list(glob(os.path.join(self.directory_roles, '*.jpg')))

        counter = 0
        dx = self.dx
        dy = self.dy
        print('len(self.roles_images) = ', len(self.roles_images))
        if(len(self.roles_images) == 0):
            for i in range(len(images)):
                self.roles_images.append(QPixmap(images[i]))
                self.roles_images[i] = self.roles_images[i].scaled(150, 200)

                label = QtWidgets.QLabel(self.scrollAreaWidgetContentsRoles)
                label.setGeometry(QtCore.QRect(self.start_x + dx, self.start_y + dy, self.width_, self.height_))
                label.setMinimumWidth(self.width_)
                label.setMinimumHeight(self.height_)
                label.setAlignment(QtCore.Qt.AlignCenter)
                label.setObjectName(str("labelRoles" + str(i)))

                self.roles_labels.append(label)

                counter = counter + 1
                if(counter % self.cards_in_row == 0):
                    dx = self.dx
                    dy = dy + self.height_ + self.dy
                else:
                    dx = dx + self.width_ + self.dx

        # Добавление groupBox и GridLayout
        #if(len(self.gridLayoutRoles) == 0):
        x_counter = 0
        y_counter = 0
        for i in range(len(self.roles_labels)):
            self.gridLayoutRoles.addWidget(self.roles_labels[i], y_counter, x_counter, 1, 1)

            if((x_counter + 1) % self.cards_in_row == 0):
                x_counter = 0
                y_counter = y_counter + 1
            else:
                x_counter = x_counter + 1

    def loadCharactersImages(self):
        images = list(glob(os.path.join(self.directory_characters, '*.jpg')))

        counter = 0
        dx = self.dx
        dy = self.dy
        if(len(self.characters_images) == 0):
            for i in range(len(images)):
                self.characters_images.append(QPixmap(images[i]))
                self.characters_images[i] = self.characters_images[i].scaled(150, 200)

                label = QtWidgets.QLabel(self.scrollAreaWidgetContentsCharacters)
                label.setGeometry(QtCore.QRect(self.start_x + dx, self.start_y + dy, self.width_, self.height_))
                label.setMinimumWidth(self.width_)
                label.setMinimumHeight(self.height_)
                label.setAlignment(QtCore.Qt.AlignCenter)
                label.setObjectName(str("labelCharacters" + str(i)))

                self.characters_labels.append(label)

                counter = counter + 1
                if(counter % self.cards_in_row == 0):
                    dx = self.dx
                    dy = dy + self.height_ + self.dy
                else:
                    dx = dx + self.width_ + self.dx

        # Добавление groupBox и GridLayout
        #if(len(self.gridLayoutCharacters) == 0):
        x_counter = 0
        y_counter = 0
        for i in range(len(self.characters_labels)):
            self.gridLayoutCharacters.addWidget(self.characters_labels[i], y_counter, x_counter, 1, 1)

            if((x_counter + 1) % self.cards_in_row == 0):
                x_counter = 0
                y_counter = y_counter + 1
            else:
                x_counter = x_counter + 1

    def loadGameCards(self):
        images = list(glob(os.path.join(self.directory_game_cards, '*.jpg')))

        counter = 0
        dx = self.dx
        dy = self.dy
        if(len(self.game_cards_images) == 0):
            for i in range(len(images)):
                self.game_cards_images.append(QPixmap(images[i]))
                self.game_cards_images[i] = self.game_cards_images[i].scaled(150, 200)

                label = QtWidgets.QLabel(self.scrollAreaWidgetContentsGameCards)
                label.setGeometry(QtCore.QRect(self.start_x + dx, self.start_y + dy, self.width_, self.height_))
                label.setMinimumWidth(self.width_)
                label.setMinimumHeight(self.height_)
                label.setAlignment(QtCore.Qt.AlignCenter)
                label.setObjectName(str("labelGameCards" + str(i)))

                self.game_cards_labels.append(label)

                counter = counter + 1
                if(counter % self.cards_in_row == 0):
                    dx = self.dx
                    dy = dy + self.height_ + self.dy
                else:
                    dx = dx + self.width_ + self.dx

        # Добавление groupBox и GridLayout
        #if(len(self.gridLayoutGameCards) == 0):
        x_counter = 0
        y_counter = 0
        for i in range(len(self.game_cards_labels)):
            self.gridLayoutGameCards.addWidget(self.game_cards_labels[i], y_counter, x_counter, 1, 1)

            if((x_counter + 1) % self.cards_in_row == 0):
                x_counter = 0
                y_counter = y_counter + 1
            else:
                x_counter = x_counter + 1

    def setImages(self):
        for i in range(len(self.roles_labels)):
            if not sip.isdeleted(self.roles_labels[i]):
                self.roles_labels[i].setPixmap(self.roles_images[i])

        for i in range(len(self.characters_labels)):
            if not sip.isdeleted(self.characters_labels[i]):
                self.characters_labels[i].setPixmap(self.characters_images[i])

        for i in range(len(self.game_cards_labels)):
            if not sip.isdeleted(self.game_cards_labels[i]):
                self.game_cards_labels[i].setPixmap(self.game_cards_images[i])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CardsWindow = QtWidgets.QMainWindow()
    ui = Ui_CardsWindow()
    ui.setupUi(CardsWindow)
    CardsWindow.show()
    sys.exit(app.exec_())
