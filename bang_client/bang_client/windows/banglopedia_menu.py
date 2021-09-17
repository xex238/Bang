import windows.base_windows.banglopedia_menu

import windows.rules
import windows.cards
import windows.main_menu

import sys
from PyQt5 import QtWidgets

class banglopedia_menu_class(QtWidgets.QWidget, windows.base_windows.banglopedia_menu.Ui_BanglopediaWindow):
    def __init__(self, mainWindow):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)

        self.buttonHowToPlay.clicked.connect(lambda: self.buttonHowToPlayClicked(mainWindow))
        self.buttonRolesCards.clicked.connect(lambda: self.buttonRolesCardsClicked(mainWindow))
        self.buttonCharactersCards.clicked.connect(lambda: self.buttonCharactersCardsClicked(mainWindow))
        self.buttonGameCards.clicked.connect(lambda: self.buttonGameCardsClicked(mainWindow))
        self.buttonMainMenu.clicked.connect(lambda: self.buttonBackClicked(mainWindow))

    def buttonHowToPlayClicked(self, mainWindow):
        rules = windows.rules.rules_class(mainWindow)

    def buttonRolesCardsClicked(self, mainWindow):
        MainWindow = QtWidgets.QMainWindow()
        cards = windows.cards.cards_class(MainWindow, 0)
        MainWindow.show()

        # cards = windows.cards.cards_class(mainWindow, 0)

    def buttonCharactersCardsClicked(self, mainWindow):
        MainWindow = QtWidgets.QMainWindow()
        cards = windows.cards.cards_class(MainWindow, 1)
        MainWindow.show()

    def buttonGameCardsClicked(self, mainWindow):
        MainWindow = QtWidgets.QMainWindow()
        cards = windows.cards.cards_class(MainWindow, 2)
        MainWindow.show()

    def buttonBackClicked(self, mainWindow):
        main_menu = windows.main_menu.main_menu_class(mainWindow)