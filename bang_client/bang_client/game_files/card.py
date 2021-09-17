class card_class:
    id = None # ID карты (из таблицы Cards)
    name = None # Имя карты
    image = None # Картинка карты
    location = None # Нахождение карты

    def __init__(self, id, name, image, location):
        self.id = id
        self.name = name
        self.image = image
        self.location = location