from PyQt5.QtGui import QPixmap

import windows.base_windows.settings

import clicked_label
import windows.main_menu
import game_process

import sys
from PyQt5 import QtWidgets

class settings_class(QtWidgets.QWidget, windows.base_windows.settings.Ui_SettingsWindow):
    imageLabelBackFile = 'images/icons/arrows/006-arrow.png'
    imageLabelOnFile = 'images/icons/music/077-volume.png'
    imageLabelOffFile = 'images/icons/music/048-mute.png'

    imageLabelOn = None
    imageLabelOff = None

    gp = None

    def __init__(self, mainWindow):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)

        self.loadSettings()
        self.loadLabels()

        self.labelBack.clicked.connect(lambda: self.labelBackClicked(mainWindow))
        self.labelMusicOnOff.clicked.connect(lambda: self.labelMusicOnOffClicked())

        self.buttonMusicMinus.clicked.connect(lambda: self.buttonMusicMinusClicked())
        self.buttonMusicPlus.clicked.connect(lambda: self.buttonMusicPlusClicked())
        self.buttonMusicVolumeMinus.clicked.connect(lambda: self.buttonMusicVolumeMinusClicked())
        self.buttonMusicVolumePlus.clicked.connect(lambda: self.buttonMusicVolumePlusClicked())
        self.buttonSoundsVolumeMinus.clicked.connect(lambda: self.buttonSoundsVolumeMinusClicked())
        self.buttonSoundsVolumePlus.clicked.connect(lambda: self.buttonSoundsVolumePlusClicked())

    def loadLabels(self):
        buttonBackImage = QPixmap(self.imageLabelBackFile)
        buttonBackImage = buttonBackImage.scaled(45, 45)
        self.labelBack.setPixmap(buttonBackImage)

        self.imageLabelOn = QPixmap(self.imageLabelOnFile)
        self.imageLabelOn = self.imageLabelOn.scaled(45, 45)

        self.imageLabelOff = QPixmap(self.imageLabelOffFile)
        self.imageLabelOff = self.imageLabelOff.scaled(45, 45)

        if(self.gp.music == 'on'):
            self.labelMusicOnOff.setPixmap(self.imageLabelOn)
        elif(self.gp.music == 'off'):
            self.labelMusicOnOff.setPixmap(self.imageLabelOff)

    def loadSettings(self):
        self.gp = game_process.game_process_class()
        self.gp.loadSettings()

        self.labelVolume.setText(str(self.gp.total_music_volume))
        self.labelMusicVolume.setText(str(self.gp.music_volume))
        self.labelSoundsVolume.setText(str(self.gp.sounds_volume))

    def saveSettings(self):
        f = open(self.gp.settings_file, 'w')

        lines = []
        lines.append('music: ' + self.gp.music + '\n')
        lines.append('total_music_volume: ' + str(self.labelVolume.text()) + '\n')
        lines.append('music_volume: ' + str(self.labelMusicVolume.text()) + '\n')
        lines.append('sounds_volume: ' + str(self.labelSoundsVolume.text()) + '\n')
        lines.append('language: russian')
        f.writelines(lines)
        f.close()

    def labelBackClicked(self, mainWindow):
        self.saveSettings()
        main_menu = windows.main_menu.main_menu_class(mainWindow)

    def labelMusicOnOffClicked(self):
        if(self.gp.music == 'on'):
            self.gp.music = 'off'
            self.labelMusicOnOff.setPixmap(self.imageLabelOff)
        elif(self.gp.music == 'off'):
            self.gp.music = 'on'
            self.labelMusicOnOff.setPixmap(self.imageLabelOn)

    def buttonMusicMinusClicked(self):
        if(int(self.labelVolume.text()) > 0):
            self.labelVolume.setText(str(int(self.labelVolume.text()) - 5))
            self.gp.total_music_volume = self.gp.total_music_volume - 5

    def buttonMusicPlusClicked(self):
        if(int(self.labelVolume.text()) < 100):
            self.labelVolume.setText(str(int(self.labelVolume.text()) + 5))
            self.gp.total_music_volume = self.gp.total_music_volume + 5

    def buttonMusicVolumeMinusClicked(self):
        if(int(self.labelMusicVolume.text()) > 0):
            self.labelMusicVolume.setText(str(int(self.labelMusicVolume.text()) - 5))
            self.gp.music_volume = self.gp.music_volume - 5

    def buttonMusicVolumePlusClicked(self):
        if(int(self.labelMusicVolume.text()) < 100):
            self.labelMusicVolume.setText(str(int(self.labelMusicVolume.text()) + 5))
            self.gp.music_volume = self.gp.music_volume + 5

    def buttonSoundsVolumeMinusClicked(self):
        if(int(self.labelSoundsVolume.text()) > 0):
            self.labelSoundsVolume.setText(str(int(self.labelSoundsVolume.text()) - 5))
            self.gp.sounds_volume = self.gp.sounds_volume - 5

    def buttonSoundsVolumePlusClicked(self):
        if(int(self.labelSoundsVolume.text()) < 100):
            self.labelSoundsVolume.setText(str(int(self.labelSoundsVolume.text()) + 5))
            self.gp.sounds_volume = self.gp.sounds_volume + 5