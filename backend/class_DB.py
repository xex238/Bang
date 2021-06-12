class DB:
    # Параметры подключения к БД
    driver = "Driver={ODBC Driver 17 for SQL Server};"
    server = "Server=den1.mssql8.gear.host;"
    database = "Database=bang2;"
    user = "uid=bang2;"
    password = "pwd=Tv08Yk-D8nZ?;"
    TC = "Trusted_Connections=yes;"

    connection_string = str(driver + server + database + user + password + TC)

    # 1.1) Запрос на регистрацию - есть ли пользователь в базе данных
    registration_request = ''
    # 1.2) Регистрация пользователя
    registration = ''
    # 1.3) Авторизация пользователя - есть ли пользователь в базе данных
    authorization_request = ''
    # 1.4) Получение списка комнат
    available_rooms = ''
    # 1.5) Получение списка достижений для выбранного пользователя
    achivements_request = ''
    # 1.6) Создание комнаты
    creating_room = ''

    # 2.1.1) Добавление игрока в комнату
    add_player_to_room = ''
    # 2.1.2) Получение n случайных персонажей (без повторений)
    getting_characters = ''
    # 2.1.4) Добавление выбранного персонажа к игроку
    add_character_to_player = ''
    # 2.1.5) Добавление роли к игроку
    add_role_to_player = ''
    # 2.1.7) Получение ID пользователя по его почте и паролю
    get_user_ID = ''
    # 2.1.8) Получение ID игрока по его почте и паролю
    get_player_ID = ''
    # 2.1.9) Получение максимального количества жизней персонажа игрока
    get_max_lives = ''

    # 3.1) Установка значения хода для заданного игрока
    player_turn_state = ''
    # 3.2) Проверка на наличие заданной карты у игрока
    check_card_availability = ''
    # 3.3) Проверка на наличие заданной карты персонажа у игрока
    check_character_availability = ''
    # 3.4) Проверка возможности выстрелить в игрока (учитывается расстояние между игроками и дальность стрельбы из оружия)
    check_shoot_opportunity = ''
    # 3.5) Выдача карты игроку из колоды
    set_card_to_player_from_Deck = ''
    # 3.6) Выдача карты игроку из сброса
    set_card_to_player_from_Dropping = ''
    # 3.7) Переход карты игрока в сброс
    send_card_to_Dropping = ''
    # 3.8) Выбранный игрок теряет 1 жизнь
    lose_health = ''
    # 3.9) Выбранный игрок восстанавливает единицу здоровья
    recovery_health = ''
    # 3.10) Кража карты у игрока
    stealing_card_from_player = ''
    # 3.11) Получение списка карт, находящихся в руке у игрока
    get_player_cards = ''
    # 3.12) Установка нового оружия для игрока
    set_weapon = ''
    # 3.13) Получение карты из колоды для проверки (проверенная карта уходит в сброс)
    get_card_for_checking = ''
    # 3.14) Изменить дополнительную защиту игрока на n
    change_additional_defence_range = ''
    # 3.15) Изменить дополнительную дальность атаки игрока на n
    change_additional_attack_range = ''
    # 3.16) Проверка, есть ли у игрока на столе карта с аналогичным названием
    check_player_name_card = ''
    # 3.17) Получить карту из колоды и добавить её на стол
    set_cards_to_table = ''
    # 3.18) Передача карты игроку
    passing_card_to_player = ''
    # 3.19) Восстановление единицы жизни всем игрокам, если это возможно
    recovery_health_all_players = ''
    # 3.20) Получить верхнюю карту из колоды и добавить её в стадию выбора
    set_cards_to_selection_stage = ''
    # 3.21) Возвращение карты в колоду
    return_card_to_Deck = ''
    # 3.22) Перемешивание карт из сброса и добавление их в колоду
    shuffle_cards_in_Dropping = ''
    # 3.23) Получение значение поля [name] в таблице [Card] для заданной ID
    get_card_name = ''
    # 3.24) Процедура позволяет изменить поле [card_location] таблицы [Card] на заданное значение
    change_card_location = ''
    # 3.25) Потеря всех карт игроком
    lose_all_cards = ''
    # 3.26) Все карты игрока уходят в руку другому игроку
    send_all_cards_to_player = ''
    # 3.27) Получить ID ролей живых игроков
    get_alive_roles_ID = ''

    def __init__(self):
        self.registration_request = 'select dbo.Registration_request(\'{mail}\', \'{password}\', \'{login}\')'

        self.registration = 'exec dbo.Registration\n'
        self.registration += '@mail = \'{mail}\',\n'
        self.registration += '@password = \'{password}\',\n'
        self.registration += '@login = \'{login}\''

        self.authorization_request = 'select dbo.Authorization_request(\'{mail}\', \'{password}\')'

        self.available_rooms = 'exec dbo.Available_rooms'

        self.achivements_request = 'exec dbo.Achivements_request\n'
        self.achivements_request += '@mail = \'{mail}\',\n'
        self.achivements_request += '@password = \'{password}\''

        self.creating_room = 'exec dbo.Creating_room\n'
        self.creating_room += '@mail = \'{mail}\',\n'
        self.creating_room += '@password = \'{password}\',\n'
        self.creating_room += '@max_count_of_players = {max_count_of_players}'

        self.add_player_to_room = 'exec dbo.Add_player_to_room\n'
        self.add_player_to_room += '@mail = \'{mail}\',\n'
        self.add_player_to_room += '@password = \'{password}\',\n'
        self.add_player_to_room += '@room_ID = {room_ID}'

        self.getting_characters = 'exec dbo.Getting_characters\n'
        self.getting_characters += '@n = {n}'

        self.add_character_to_player = 'exec dbo.Add_character_to_player\n'
        self.add_character_to_player += '@player_ID = {player_ID},\n'
        self.add_character_to_player += '@characters_ID = {characters_ID}'

        self.add_role_to_player = 'exec dbo.Add_role_to_player\n'
        self.add_role_to_player += '@player_ID = {player_ID},\n'
        self.add_role_to_player += '@roles_ID = {roles_ID}'

        self.get_user_ID = 'exec dbo.Get_user_ID\n'
        self.get_user_ID += '@mail = \'{mail}\',\n'
        self.get_user_ID += '@password = \'{password}\''

        self.get_player_ID = 'exec dbo.Get_player_ID\n'
        self.get_player_ID += '@mail = \'{mail}\',\n'
        self.get_player_ID += '@password = \'{password}\''

        self.get_max_lives = 'exec dbo.Get_max_lives\n'
        self.get_max_lives += '@player_ID = {player_ID}'

        self.player_turn_state = 'exec dbo.Player_turn_state\n'
        self.player_turn_state += '@player_ID = {player_ID},\n'
        self.player_turn_state += '@state = {state}'

        self.check_card_availability = 'select dbo.Check_card_availability({player_ID}, {card_ID})'

        self.check_character_availability = 'select dbo.Check_character_availability({player_ID}, {character_ID})'

        self.check_shoot_opportunity = 'select dbo.Check_shoot_opportunity({player_ID}, {target_ID})'

        self.set_card_to_player_from_Deck = 'exec dbo.Set_card_to_player_from_Deck\n'
        self.set_card_to_player_from_Deck += '@player_ID = {player_ID},\n'
        self.set_card_to_player_from_Deck += '@room_ID = {room_ID}'

        self.set_card_to_player_from_Dropping = 'exec dbo.Set_card_to_player_from_Dropping\n'
        self.set_card_to_player_from_Dropping += '@player_ID = {player_ID},\n'
        self.set_card_to_player_from_Dropping += '@room_ID = {room_ID}'

        self.send_card_to_Dropping = 'exec dbo.Send_card_to_Dropping\n'
        self.send_card_to_Dropping += '@card_ID = {card_ID},\n'
        self.send_card_to_Dropping += '@room_ID = {room_ID}'

        self.lose_health = 'exec dbo.Lose_health\n'
        self.lose_health += '@player_ID = {player_ID}'

        self.recovery_health = 'exec dbo.Recovery_health\n'
        self.recovery_health += '@player_ID = {player_ID}'

        self.stealing_card_from_player = 'exec dbo.Stealing_card_from_player\n'
        self.stealing_card_from_player += '@player_ID_to = {player_ID_to},\n'
        self.stealing_card_from_player += '@card_ID = {card_ID}'

        self.get_player_cards = 'exec dbo.Get_player_cards\n'
        self.get_player_cards += '@player_ID = {player_ID}'

        self.set_weapon = 'exec dbo.Set_weapon\n'
        self.set_weapon += '@player_ID = {player_ID},\n'
        self.set_weapon += '@name = \'{name}\',\n'
        self.set_weapon += '@base_weapon = {base_weapon},\n'
        self.set_weapon += '@firing_range = {firing_range},\n'
        self.set_weapon += '@endless_bang = {endless_bang},\n'
        self.set_weapon += '@weapon_card_ID = {weapon_card_ID},\n'
        self.set_weapon += '@room_ID = {room_ID}'

        self.get_card_for_checking = 'exec dbo.Get_card_for_checking\n'
        self.get_card_for_checking += '@room_ID = {room_ID}'

        self.change_additional_defence_range = 'exec dbo.Change_additional_defence_range\n'
        self.change_additional_defence_range += '@player_ID = {player_ID},\n'
        self.change_additional_defence_range += '@n = {n}'

        self.change_additional_attack_range = 'exec dbo.Change_additional_attack_range\n'
        self.change_additional_attack_range += '@player_ID = {player_ID},\n'
        self.change_additional_attack_range += '@n = {n}'

        self.check_player_name_card = 'exec dbo.Check_player_name_card\n'
        self.check_player_name_card += '@player_ID = {player_ID},\n'
        self.check_player_name_card += '@name = \'{name}\''

        self.set_cards_to_table = 'exec dbo.Set_cards_to_table\n'
        self.set_cards_to_table += '@room_ID = {room_ID}'

        self.passing_card_to_player = 'exec dbo.Passing_card_to_player\n'
        self.passing_card_to_player += '@player_ID = {player_ID},\n'
        self.passing_card_to_player += '@card_ID = {card_ID},\n'
        self.passing_card_to_player += '@card_location = {card_location}'

        self.recovery_health_all_players = 'exec dbo.Recovery_health_all_players\n'
        self.recovery_health_all_players += '@room_ID = {room_ID}'

        self.set_cards_to_selection_stage = 'exec dbo.Set_cards_to_selection_stage\n'
        self.set_cards_to_selection_stage += '@room_ID = {room_ID}'

        self.return_card_to_Deck = 'exec dbo.Return_card_to_Deck\n'
        self.return_card_to_Deck += '@card_ID = {card_ID},\n'
        self.return_card_to_Deck += '@room_ID = {room_ID}'

        self.shuffle_cards_in_Dropping = 'exec dbo.Shuffle_cards_in_Dropping\n'
        self.shuffle_cards_in_Dropping += '@room_ID = {room_ID}'

        self.get_card_name = 'exec dbo.Get_card_name\n'
        self.get_card_name += '@card_ID = {card_ID}'

        self.change_card_location = 'exec dbo.Change_card_location\n'
        self.change_card_location += '@card_ID = {card_ID},\n'
        self.change_card_location += '@card_location = {card_location}'

        self.lose_all_cards = 'exec dbo.Lose_all_cards\n'
        self.lose_all_cards += '@player_ID = {player_ID},\n'
        self.lose_all_cards += '@room_ID = {room_ID}'

        self.send_all_cards_to_player = 'exec dbo.Send_all_cards_to_player\n'
        self.send_all_cards_to_player += '@player_ID_from = {player_ID_from},\n'
        self.send_all_cards_to_player += '@player_ID_to = {player_ID_to}'

        self.get_alive_roles_ID = 'exec dbo.Get_alive_roles_ID\n'
        self.get_alive_roles_ID += '@room_ID = {room_ID}'