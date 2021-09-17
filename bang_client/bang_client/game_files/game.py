class game_class:
    # Количество игроков
    count_of_players = None

    # Уровень сложности
    level = None

    # Игроки
    players = []

    # Карты в колоде
    deck_cards = []
    # Карты в сбросе
    dropping_cards = []

    def __init__(self, count_of_players, level):
        self.count_of_players = count_of_players
        self.level = level

    def generateRoles(self):
