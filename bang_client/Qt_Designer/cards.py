# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cards.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CardsWindow(object):
    def setupUi(self, CardsWindow):
        CardsWindow.setObjectName("CardsWindow")
        CardsWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(CardsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelBack = QtWidgets.QLabel(self.centralwidget)
        self.labelBack.setGeometry(QtCore.QRect(15, 15, 48, 48))
        self.labelBack.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBack.setObjectName("labelBack")
        self.tabWidgetCards = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidgetCards.setGeometry(QtCore.QRect(75, 75, 933, 737))
        self.tabWidgetCards.setObjectName("tabWidgetCards")
        self.tabRoles = QtWidgets.QWidget()
        self.tabRoles.setObjectName("tabRoles")
        self.scrollArea = QtWidgets.QScrollArea(self.tabRoles)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 901, 601))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 882, 1024))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.labelTest_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelTest_2.setMinimumSize(QtCore.QSize(0, 500))
        self.labelTest_2.setObjectName("labelTest_2")
        self.gridLayout.addWidget(self.labelTest_2, 1, 0, 1, 1)
        self.labelTest_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelTest_1.setMinimumSize(QtCore.QSize(0, 500))
        self.labelTest_1.setObjectName("labelTest_1")
        self.gridLayout.addWidget(self.labelTest_1, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidgetCards.addTab(self.tabRoles, "")
        self.tabCharacters = QtWidgets.QWidget()
        self.tabCharacters.setObjectName("tabCharacters")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tabCharacters)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 911, 601))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayoutCharacters = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayoutCharacters.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutCharacters.setObjectName("gridLayoutCharacters")
        self.tabWidgetCards.addTab(self.tabCharacters, "")
        self.tabGameCards = QtWidgets.QWidget()
        self.tabGameCards.setObjectName("tabGameCards")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tabGameCards)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 911, 601))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayoutGameCards = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayoutGameCards.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutGameCards.setObjectName("gridLayoutGameCards")
        self.tabWidgetCards.addTab(self.tabGameCards, "")
        CardsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CardsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        CardsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CardsWindow)
        self.statusbar.setObjectName("statusbar")
        CardsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CardsWindow)
        self.tabWidgetCards.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CardsWindow)

    def retranslateUi(self, CardsWindow):
        _translate = QtCore.QCoreApplication.translate
        CardsWindow.setWindowTitle(_translate("CardsWindow", "Карты"))
        self.labelBack.setText(_translate("CardsWindow", "<"))
        self.labelTest_2.setText(_translate("CardsWindow", "TextLabel"))
        self.labelTest_1.setText(_translate("CardsWindow", "TextLabel"))
        self.tabWidgetCards.setTabText(self.tabWidgetCards.indexOf(self.tabRoles), _translate("CardsWindow", "Роли"))
        self.tabWidgetCards.setTabText(self.tabWidgetCards.indexOf(self.tabCharacters), _translate("CardsWindow", "Персонажи"))
        self.tabWidgetCards.setTabText(self.tabWidgetCards.indexOf(self.tabGameCards), _translate("CardsWindow", "Игровые карты"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CardsWindow = QtWidgets.QMainWindow()
    ui = Ui_CardsWindow()
    ui.setupUi(CardsWindow)
    CardsWindow.show()
    sys.exit(app.exec_())