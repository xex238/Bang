from PyQt5.QtWidgets import QGroupBox, QGridLayout, QVBoxLayout

import windows.base_windows.cards

import windows.banglopedia_menu

import sys
import os
from glob import glob

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap

class cards_class(QtWidgets.QWidget, windows.base_windows.cards.Ui_CardsWindow):
    def __init__(self, mainWindow, currentPage):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)

        self.tabWidgetCards.setCurrentIndex(currentPage)
        # self.labelBack.clicked.connect(lambda: self.labelBackClicked(mainWindow))

        # if(len(self.roles_images) == 0):
        #     self.loadImages(mainWindow)
        #     # self.retranslateUi(CardsWindow)
        #     # QtCore.QMetaObject.connectSlotsByName(CardsWindow)
        # else:
        #     #self.retranslateUi2(mainWindow)
        #     #self.setImages(mainWindow)
        #
        #     #QtCore.QMetaObject.connectSlotsByName(mainWindow)

    # def loadImages(self, mainWindow):
    #     self.loadRolesImages(mainWindow)
    #     self.loadCharactersImages(mainWindow)
    #     self.loadGameCards(mainWindow)
    #
    #     self.retranslateUi2(mainWindow)
    #     QtCore.QMetaObject.connectSlotsByName(mainWindow)
    #
    #     self.setImages(mainWindow)
    #
    # def loadRolesImages(self, mainWindow):
    #     images = list(glob(os.path.join(self.directory_roles, '*.jpg')))
    #
    #     counter = 0
    #     dx = self.dx
    #     dy = self.dy
    #     for i in range(len(images)):
    #         self.roles_images.append(QPixmap(images[i]))
    #         self.roles_images[i] = self.roles_images[i].scaled(150, 200)
    #
    #         label = QtWidgets.QLabel(self.tabRoles)
    #         label.setGeometry(QtCore.QRect(self.start_x + dx, self.start_y + dy, self.width, self.height))
    #         label.setAlignment(QtCore.Qt.AlignCenter)
    #         label.setObjectName(str("labelRoles" + str(i)))
    #
    #         self.roles_labels.append(label)
    #
    #         counter = counter + 1
    #         if(counter % self.cards_in_row == 0):
    #             dx = self.dx
    #             dy = dy + self.height + self.dy
    #         else:
    #             dx = dx + self.width + self.dx
    #
    #     # Добавление groupBox и GridLayout
    #     x_counter = 0
    #     y_counter = 0
    #     for i in range(len(self.roles_labels)):
    #         self.gridLayoutRoles.addWidget(self.roles_labels[i], y_counter, x_counter)
    #
    #         if((x_counter + 1) % self.cards_in_row == 0):
    #             x_counter = 0
    #             y_counter = y_counter + 1
    #         else:
    #             x_counter = x_counter + 1
    #
    # def loadCharactersImages(self, mainWindow):
    #     images = list(glob(os.path.join(self.directory_characters, '*.jpg')))
    #
    #     counter = 0
    #     dx = self.dx
    #     dy = self.dy
    #     for i in range(len(images)):
    #         self.characters_images.append(QPixmap(images[i]))
    #         self.characters_images[i] = self.characters_images[i].scaled(150, 200)
    #
    #         label = QtWidgets.QLabel(self.tabCharacters)
    #         label.setGeometry(QtCore.QRect(self.start_x + dx, self.start_y + dy, self.width, self.height))
    #         label.setAlignment(QtCore.Qt.AlignCenter)
    #         label.setObjectName(str("labelCharacters" + str(i)))
    #
    #         self.characters_labels.append(label)
    #
    #         counter = counter + 1
    #         if(counter % self.cards_in_row == 0):
    #             dx = self.dx
    #             dy = dy + self.height + self.dy
    #         else:
    #             dx = dx + self.width + self.dx
    #
    #     # Добавление groupBox и GridLayout
    #     x_counter = 0
    #     y_counter = 0
    #     for i in range(len(self.characters_labels)):
    #         self.gridLayoutCharacters.addWidget(self.characters_labels[i], y_counter, x_counter)
    #
    #         if((x_counter + 1) % self.cards_in_row == 0):
    #             x_counter = 0
    #             y_counter = y_counter + 1
    #         else:
    #             x_counter = x_counter + 1
    #
    # def loadGameCards(self, mainWindow):
    #     images = list(glob(os.path.join(self.directory_game_cards, '*.jpg')))
    #
    #     counter = 0
    #     dx = self.dx
    #     dy = self.dy
    #     for i in range(len(images)):
    #         self.game_cards_images.append(QPixmap(images[i]))
    #         self.game_cards_images[i] = self.game_cards_images[i].scaled(150, 200)
    #
    #         label = QtWidgets.QLabel(self.tabGameCards)
    #         label.setGeometry(QtCore.QRect(self.start_x + dx, self.start_y + dy, self.width, self.height))
    #         label.setAlignment(QtCore.Qt.AlignCenter)
    #         label.setObjectName(str("labelGameCards" + str(i)))
    #
    #         self.game_cards_labels.append(label)
    #
    #         counter = counter + 1
    #         if(counter % self.cards_in_row == 0):
    #             dx = self.dx
    #             dy = dy + self.height + self.dy
    #         else:
    #             dx = dx + self.width + self.dx
    #
    #     # Добавление groupBox и GridLayout
    #     x_counter = 0
    #     y_counter = 0
    #     for i in range(len(self.game_cards_labels)):
    #         self.gridLayoutGameCards.addWidget(self.game_cards_labels[i], y_counter, x_counter)
    #
    #         if((x_counter + 1) % self.cards_in_row == 0):
    #             x_counter = 0
    #             y_counter = y_counter + 1
    #         else:
    #             x_counter = x_counter + 1
    #
    # def retranslateUi2(self, mainWindow):
    #     _translate = QtCore.QCoreApplication.translate
    #     mainWindow.setWindowTitle(_translate("CardsWindow", "Карты"))
    #
    #     for i in range(len(self.roles_labels)):
    #         self.roles_labels[i].setText(_translate("CardsWindow", str("labelRules" + str(i))))
    #
    #     for i in range(len(self.characters_labels)):
    #         self.characters_labels[i].setText(_translate("CardsWindow", str("labelCharacters" + str(i))))
    #
    #     for i in range(len(self.game_cards_labels)):
    #         self.game_cards_labels[i].setText(_translate("CardsWindow", str("labelGameCards" + str(i))))

    # def setImages(self, mainWindow):
    #     for i in range(len(self.roles_labels)):
    #         self.roles_labels[i].setPixmap(self.roles_images[i])
    #
    #     for i in range(len(self.characters_labels)):
    #         self.characters_labels[i].setPixmap(self.characters_images[i])
    #
    #     for i in range(len(self.game_cards_labels)):
    #         self.game_cards_labels[i].setPixmap(self.game_cards_images[i])

    def labelBackClicked(self, mainWindow):
        banglopedia_menu = windows.banglopedia_menu.banglopedia_menu_class(mainWindow)