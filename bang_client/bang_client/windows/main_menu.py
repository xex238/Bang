import windows.base_windows.main_menu

#import windows.single1
import windows.loading
import windows.online1
import windows.choice_room
import windows.banglopedia_menu
import windows.settings
import windows.statistics
import windows.callback
import game_process

import sys
from PyQt5 import QtWidgets

class main_menu_class(QtWidgets.QWidget, windows.base_windows.main_menu.Ui_MainWindow):
    def __init__(self, mainWindow):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)

        self.button_single_mode.clicked.connect(lambda: self.buttonSingleModeClicked(mainWindow))
        self.button_multi_mode.clicked.connect(lambda: self.buttonMultiModeClicked(mainWindow))
        self.button_banglopedia.clicked.connect(lambda: self.buttonBanglopediaClicked(mainWindow))
        self.button_settings.clicked.connect(lambda: self.buttonSettingsClicked(mainWindow))
        self.button_statistics.clicked.connect(lambda: self.buttonStatisticsClicked(mainWindow))
        self.button_callback.clicked.connect(lambda: self.buttonCallbackClicked(mainWindow))
        self.button_exit.clicked.connect(lambda: self.buttonExitClicked())

    def buttonSingleModeClicked(self, mainWindow):
        # single1 = windows.single1.single1_class(mainWindow)
        loading = windows.loading.loading_class(mainWindow)

    def buttonMultiModeClicked(self, mainWindow):
        gp = game_process.game_process_class()

        if(gp.mail == "" or gp.password == "" or gp.login == ""):
            online1 = windows.online1.online1_class(mainWindow)
        else:
            choice_room = windows.choice_room.choice_room_class(mainWindow)

    def buttonBanglopediaClicked(self, mainWindow):
        banglopedia_menu = windows.banglopedia_menu.banglopedia_menu_class(mainWindow)

    def buttonSettingsClicked(self, mainWindow):
        settings = windows.settings.settings_class(mainWindow)

    def buttonStatisticsClicked(self, mainWindow):
        statistics = windows.statistics.statistics_class(mainWindow)

    def buttonCallbackClicked(self, mainWindow):
        callback = windows.callback.callback_class(mainWindow)

    def buttonExitClicked(self):
        exit(0)