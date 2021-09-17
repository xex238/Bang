# Класс для хранения данных основных параметров игры
class game_process_class:
    registration_file = 'data_files/user_files/registration.txt'
    statistics_file = 'data_files/user_files/statistics.txt'
    settings_file = 'data_files/user_files/settings.txt'

    roles_file = 'data_files/game_files/roles.txt'
    characters_file = 'data_files/game_files/characters.txt'

    # Данные для регистрации по сети
    mail = None
    login = None
    password = None

    # Данные о сохранённых играх в одиночном режиме
    games = []

    # Статистические данные за прошлые игры
    statistics = []

    # Параметры громкости звука
    music = 'on'
    total_music_volume = 50
    music_volume = 50
    sounds_volume = 50
    language = 'russian'

    # Словарь персонажей и их ID значений из таблицы [Characters]
    character_names = []
    character_number = []

    # Словарь ролей и их значений ID из таблицы [Roles]
    roles_names = []
    roles_number = []

    # Загрузка пользовательских данных с файла
    # Загрузка данных о сохранённых играх в одиночном режиме
    # Загрузка статистических данных за прошлые игры
    # Загрузка данных о громкости звука

    def loadData(self):
        self.loadRegistrationData()
        self.loadStatistics()
        self.loadSettings()

        self.loadRoles()
        self.loadCharacters()

    def loadRegistrationData(self):
        f = open(self.registration_file, 'r')
        lines = f.readlines()
        f.close()

        for i in range(len(lines) - 1):
            lines[i] = lines[i][:-1]

        for i in range(len(lines)):
            lines[i] = lines[i].split(':')[1][1:]

        self.mail = lines[0]
        self.login = int(lines[1])
        self.password = int(lines[2])

    def loadStatistics(self):
        f = open(self.statistics_file, 'r')
        lines = f.readlines()
        f.close()

        for i in range(len(lines) - 1):
            lines[i] = lines[i][:-1]

        for i in range(len(lines)):
            lines[i] = lines[i].split(':')[1][1:]

        for i in range(len(lines)):
            self.statistics.append(lines[i])

    def loadSettings(self):
        f = open(self.settings_file, 'r')
        lines = f.readlines()
        f.close()

        for i in range(len(lines) - 1):
            lines[i] = lines[i][:-1]

        for i in range(len(lines)):
            lines[i] = lines[i].split(':')[1][1:]

        self.music = str(lines[0])
        self.total_music_volume = int(lines[1])
        self.music_volume = int(lines[2])
        self.sounds_volume = int(lines[3])
        self.language = str(lines[4])

    def loadRoles(self):
        f = open(self.roles_file, 'r')
        lines = f.readlines()
        f.close()

        for i in range(len(lines) - 1):
            lines[i] = lines[i][:-1]

        for i in range(len(lines)):
            self.roles_names = lines[i].split(':')[0]
            self.roles_number = lines[i].split(':')[1][1:]

    def loadCharacters(self):
        f = open(self.characters_file, 'r')
        lines = f.readlines()
        f.close()

        for i in range(len(lines) - 1):
            lines[i] = lines[i][:-1]

        for i in range(len(lines)):
            self.character_names = lines[i].split(':')[0]
            self.character_number = lines[i].split(':')[1][1:]