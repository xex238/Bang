import asyncio
import websockets

import os
import pyodbc

import random
import math

import class_DB
import class_request

class Room:
    room_ID = -1 # ID комнаты (аналогичен значению в БД)
    room_status = "open" # Статус комнаты (аналогичен значению в БД)
    room_IP = None # IP адрес комнаты
    room_port = None # Порт комнаты

    server = None # Сервер комнаты

    DB = class_DB.DB() # Экземпляр класса DB, в котором хранятся строки для вызова процедур/функций из базы данных
    requests = class_request.request()

    max_count_of_players = -1 # Максимальное количество игроков в комнате
    count_of_players = 0 # Текущее количество игроков в комнате

    players_ID = [] # Список ID участников комнаты
    players_status = [] # Список статусов участников комнаты (для начала стадии планирования,
    # Для начала передачи информации о других игроках после выбора персонажа и роли, для начала игры)
    players_IP = [] # Список IP адресов участников комнаты
    players_port = [] # Список портов участников комнаты

    players_roles_ID = [] # Список ID ролей участников комнаты
    players_characters_ID = [] # Список ID персонажей участников комнаты

    players_queue = [] # Очередь хода игрока (по часовой стрелке, начиная от шерифа, шериф имеет значение 1)
    players_alive = [] # Жив ли игрок?
    count_of_alive = -1 # Количество живых персонажей
    current_i_queue = -1 # Указатель на номер элемента в массиве "players_queue"
    current_queue = -1 # Порядковый номер хода (по часовой стрелке)

    # Вспомогательные переменные для розыгрыша карт "Гатлинг" и "Индейцы"
    current_i_queue_helper = -1 # Вспомогательная переменная, аналог переменной "current_i_queue"
    current_queue_helper = -1 # Вспомогательная переменная, аналог переменной "current_queue"
    counter_helper = -1 # Вспомогательная переменная

    vulture_sam_player_ID = -1 # ID игрока, у которого персонаж "Большой Змей" (Vulture Sam)

    count_of_cards_in_deck = 80 # Количество карт в колоде
    count_of_cards_in_dropping = 0 # Количество карт в сбросе

    cards_ID_to_dropping = [] # Список карт, которые необходимо будет отправить в сброс

    # Словарь персонажей и их ID значений из таблицы [Characters]
    dict_characters = {
    "bart_cassidy": 1,
    "black_jack": 2,
    "calamity_janet": 3,
    "el_gringo": 4,
    "jesse_jones": 5,
    "jourdonnais": 6,
    "kit_carison": 7,
    "lucky_duke": 8,
    "paul_regret": 9,
    "pedro_ramires": 10,
    "rose_doolan": 11,
    "sid_ketchum": 12,
    "slab_the_killer": 13,
    "suzy_lafayette": 14,
    "vulture_sam": 15,
    "willy_the_kid": 16
    }

    # Словарь ролей и их значений ID из таблицы [Roles]
    dict_roles = {
    "sheriff": 1,
    "outlaw": 2,
    "renegate": 3,
    "deputy": 4}

    def __init__(self, max_count_of_players, room_ID, room_IP, room_port):
        self.max_count_of_players = max_count_of_players

        self.room_ID = room_ID
        self.room_status = "open"
        self.room_IP = room_IP
        self.room_port = room_port

    def Start_server(self):
        main_server = websockets.serve(self.Data_exchange, "localhost", self.room_port)
        asyncio.get_event_loop().run_until_complete(main_server)
        asyncio.get_event_loop().run_forever()

    # Возвращение порядкового номера в массиве по ID
    def Get_i(self, player_ID):
        for i in range(len(self.players_ID)):
            if(self.players_ID[i] == player_ID):
                return i

    def Get_i_queue(self, value):
        for i in range(len(self.players_queue)):
            if(self.players_queue[i] == value):
                return i

    # Открытие (запуск) комнаты
    def Start_room(self):
        self.server = websockets.serve(self.Data_exchange, self.room_IP, self.room_port)
        asyncio.get_event_loop().run_until_complete(self.server)
        asyncio.get_event_loop().run_forever()

    # Отправка сообщения одному игроку
    async def Send(self, message, i, player_ID):
        #uri = "ws://" + str(self.room_IP[i]) + ":" + str(self.room_port[i])
        uri = "ws://" + str(self.players_IP[i]) + ":" + str(self.players_port[i])
        print(uri)
        async with websockets.connect(uri) as websocket:
            print("Всё ок!")
            await websocket.send(message)

    # Отправка сообщения всем игрокам
    async def Send_all(self, message):
        for i in range(len(self.players_ID)):
            uri = "ws://" + self.room_IP[i] + ":" + self.room_port[i]
            async with websockets.connect(uri) as websocket:
                await websocket.send(message)

    # Отправка сообщения всем игрокам, кроме одного
    async def Send_all_except_one(self, message, player_ID):
        for i in range(len(self.players_ID)):
            if(self.players_ID[i] != player_ID):
                uri = "ws://" + self.room_IP[i] + ":" + self.room_port[i]
                async with websockets.connect(uri) as websocket:
                    await websocket.send(message)

    # Очистка списка карт, которые необходимо отправит в сброс
    def Cards_to_Dropping(self):
        for i in range(len(self.cards_ID_to_dropping)):
            cursor = self.conn.cursor()
            cursor.execute(self.DB.send_card_to_Dropping.format(card_ID = str(self.cards_ID_to_dropping[i]), room_ID = str(self.room_ID)))
            cursor.commit()

        self.cards_ID_to_dropping.clear()

    # Отправка заданной карты в сброс
    def Send_card_to_Dropping(self, card_ID):
        cursor = self.conn.cursor()
        cursor.execute(self.DB.send_card_to_Dropping.format(card_ID = str(card_ID), room_ID = str(self.room_ID)))
        cursor.commit()

    # Получить карту из сброса и присвоить её игроку
    def Set_card_to_player_from_Dropping(self, player_ID):
        cursor = self.conn.cursor()
        cursor.execute(self.DB.Set_card_to_player_from_Dropping.format(player_ID = str(player_ID), room_ID = str(self.room_ID)))
        dropping_card_ID = str(cursor.fetchall()[0][0])
        cursor.commit()

        return dropping_card_ID

    # Получить карту из колоды
    async def Get_card_from_Deck(self, player_ID, websocket):
        cursor = self.conn.cursor()
        cursor.execute(self.DB.set_card_to_player_from_Deck.format(player_ID = str(player_ID), room_ID = str(self.room_ID)))
        deck_card_ID = str(cursor.fetchall()[0][0])
        cursor.commit()

        request = "GET 1 CARD\n"
        request += str(deck_card_ID)

        await websocket.send(request)

    # Реализация розыгрыша карты "Мимо"
    async def Play_missed(self, message, player_ID, card_ID, message_split):
        self.Send_card_to_Dropping(int(card_ID))
        if(len(message_split) == 3):
            self.Cards_to_Dropping()

        request = message
        asyncio.get_event_loop().run_until_complete(self.Send_all(request))

        if(len(message_split) > 3):
            if((message_split[3] == "PLAY GATLING") and (self.counter_helper + 1 < self.count_of_alive)):
                self.counter_helper = self.counter_helper + 1

                while(true):
                    if(self.current_queue + 1 <= self.max_count_of_players):
                        self.current_queue_helper = self.current_queue + 1
                    else:
                        self.current_queue_helper = 1
                    self.current_i_queue_helper = self.Get_i_queue(self.current_queue_helper)
                    if(self.players_alive[self.current_i_queue_helper] == 1):
                        break

                request = "PLAY GATLING\n"
                request += str(player_ID) + ", " + str(self.players_ID[self.current_i_queue_helper]) + "\n"
                request += str(self.cards_ID_to_dropping[0])
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            elif((message_split[3] == "PLAY GATLING") and (self.counter_helper + 1 == self.count_of_alive)):
                self.Cards_to_Dropping()

            asyncio.get_event_loop().run_until_complete(self.Send_all(request))

    # Реализация проверки
    async def Checking(self, suit_ok, rating_ok):
        cursor = self.conn.cursor()
        cursor.execute(self.DB.get_card_for_checking.format(room_ID = str(self.room_ID)))

        check_card_ID = -1
        suit = ""
        rating = ""
        for row in cursor:
            check_card_ID = int(row[0])
            suit = str(row[2])
            rating = str(row[3])
        cursor.commit()

        result = False
        if((len(rating_ok) != 0) and (len(suit_ok) != 0)):
            for i in range(len(suit_ok)):
                for j in range(len(rating_ok)):
                    if((suit_ok[i] == suit) and (rating_ok[j] == rating)):
                        result = True
                        break
        elif((len(rating_ok) != 0) and (len(suit_ok) == 0)):
            for i in range(len(rating_ok)):
                if(rating_ok[i] == rating):
                    result = True
                    break
        elif((len(rating_ok) == 0) and (len(suit_ok) != 0)):
            for i in range(len(suit_ok)):
                if(suit_ok[i] == suit):
                    result = True
                    break

        return result, check_card_ID

    # Реализация проверки бочки при выстреле
    async def Check_hit(self, message, player_ID):
        result, check_card_ID = self.Checking(["H"], [])

        if(result):
            request += "CHECK SUCCESS\n"
        else:
            request += "CHECK FAIL\n"
        request += str(check_card_ID)

        if(len(message_split) > 3):
            if(message_split[3] == "PLAY GATLING"):
                request += "\n"
                request += "PLAY GATLING"
            if((message_split[3] == "PLAY GATLING") and (self.counter_helper + 1 < self.count_of_alive) and (suit == "H")):
                self.counter_helper = self.counter_helper + 1

                while(true):
                    if(self.current_queue + 1 <= self.max_count_of_players):
                        self.current_queue_helper = self.current_queue + 1
                    else:
                        self.current_queue_helper = 1
                    self.current_i_queue_helper = self.Get_i_queue(self.current_queue_helper)
                    if(self.players_alive[self.current_i_queue_helper] == 1):
                        break

                request = "PLAY GATLING\n"
                request += str(player_ID) + ", " + str(self.players_ID[self.current_i_queue_helper]) + "\n"
                request += str(self.cards_ID_to_dropping[0])
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            elif((message_split[3] == "PLAY GATLING") and (self.counter_helper + 1 == self.count_of_alive) and (suit == "H")):
                self.Cards_to_Dropping()

        asyncio.get_event_loop().run_until_complete(self.Send_all(request))
        self.Send_card_to_Dropping(int(card_ID))
        if(len(message_split) == 3):
            self.Cards_to_Dropping()

        request = message
        asyncio.get_event_loop().run_until_complete(self.Send_all(request))

        if(len(message_split) > 3):
            if((message_split[3] == "PLAY GATLING") and (self.counter_helper + 1 < self.count_of_alive)):
                self.counter_helper = self.counter_helper + 1

                while(true):
                    if(self.current_queue + 1 <= self.max_count_of_players):
                        self.current_queue_helper = self.current_queue + 1
                    else:
                        self.current_queue_helper = 1
                    self.current_i_queue_helper = self.Get_i_queue(self.current_queue_helper)
                    if(self.players_alive[self.current_i_queue_helper] == 1):
                        break

                request = "PLAY GATLING\n"
                request += str(player_ID) + ", " + str(self.players_ID[self.current_i_queue_helper]) + "\n"
                request += str(self.cards_ID_to_dropping[0])
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            elif((message_split[3] == "PLAY GATLING") and (self.counter_helper + 1 == self.count_of_alive)):
                self.Cards_to_Dropping()

            asyncio.get_event_loop().run_until_complete(self.Send_all(request))

    # Реализация кражи карты с руки
    async def Steal_card_from_hand(self, player_ID, target_ID):
        cursor = self.conn.cursor()
        cursor.execute(self.DB.get_player_cards.format(player_ID = str(target_ID)))

        cards_ID = []
        for row in cursor:
            cards_ID.append(str(row[0]))

        target_card_ID = cards_ID[math.floor(random.random() * len(cards_ID))]

        cursor.execute(self.DB.stealing_card_from_player.format(player_ID_to = str(player_ID), card_ID = str(target_card_ID)))
        cursor.commit()

        request = "LOSE 1 CARD\n"
        request += str(target_card_ID)

        asyncio.get_event_loop().run_until_complete(self.Send(request, self.Get_i(targer_ID)))

        request = "GET 1 CARD"
        request += str(target_card_ID)

        await websocket.send(request)

    # Потеря единицы жизни игроком
    async def Lose_health(self, websocket, player_ID, killer_ID, message):
        cursor = self.conn.cursor()
        cursor.execute(self.DB.lose_health.format(player_ID = str(player_ID)))
        code = str(cursor.fetchall()[0][0])
        cursor.commit()

        request = message
        asyncio.get_event_loop().run_until_complete(self.Send_all(request))

        # Если игрок погиб
        if(code == "10"):
            self.count_of_alive = self.count_of_alive - 1
            self.players_alive[self.Get_i(player_ID)] = 0

            request = "PLAYER DIED\n"
            if(killer_ID != ""):
                request = str(player_ID) + ", " + str(killer_ID) + "\n"
            else:
                request = str(player_ID) + "\n"
            request += str(self.players_roles_ID[self.Get_i(player_ID)])

            self.players_alive[self.Get_i(player_ID)] = 0

            asyncio.get_event_loop().run_until_complete(self.Send_all(request))

            # Выполнена ли цель?
            # Получаем ID ролей оставшихся в живых игроков
            cursor.execute(self.DB.get_alive_roles_ID.format(room_ID = str(self.room_ID)))

            alive_roles_ID = []
            for row in cursor:
                alive_roles_ID.append(str(row[0]))

            # Если убит шериф
            if(self.players_roles_ID[self.Get_i(player_ID)] == 1):
                if((len(alive_roles_ID) > 1) or ((len(alive_roles_ID) == 1) and (alive_roles_ID[0] != "3"))):
                    request += "GAME OVER\n"
                    request += "OUTLAW WIN\n"
                    request += "WIN\n"
                            
                    for i in range(len(self.players_roles_ID)):
                        if(self.players_roles_ID[i] == 2):
                            request += str(self.players_ID[i]) + ", "
                    request = request[:-2]
                    request += "\n"
                    request += "LOSE\n"

                    for i in range(len(self.players_roles_ID)):
                        if(self.players_roles_ID[i] != 2):
                            request += str(self.players_ID[i]) + ", "
                    request = request[:-2]

                    asyncio.get_event_loop().run_until_complete(self.Send_all(request))
                else:
                    request += "GAME OVER\n"
                    request += "RENEGATE WIN\n"
                    request += "WIN\n"
                            
                    for i in range(len(self.players_roles_ID)):
                        if(self.players_roles_ID[i] == 3):
                            request += str(self.players_ID[i]) + ", "
                    request = request[:-2]
                    request += "\n"
                    request += "LOSE\n"

                    for i in range(len(self.players_roles_ID)):
                        if(self.players_roles_ID[i] != 3):
                            request += str(self.players_ID[i]) + ", "
                    request = request[:-2]

                    asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            elif((self.players_roles_ID[self.Get_i(player_ID)] == 2) or (self.players_roles_ID[self.Get_i(player_ID)] == 3)):
                sheriff_and_deputes_only = True
                for i in range(len(alive_roles_ID)):
                    if((alive_roles_ID[i] == "2") or (alive_roles_ID[i] == "3")):
                        sheriff_and_deputes_only = False
                        break

                if(sheriff_and_deputes_only):
                    request += "GAME OVER\n"
                    request += "SHERIFF AND DEPUTES WIN\n"
                    request += "WIN\n"
                            
                    for i in range(len(self.players_roles_ID)):
                        if((self.players_roles_ID[i] == 1) or (self.players_roles_ID[i] == 4)):
                            request += str(self.players_ID[i]) + ", "
                    request = request[:-2]
                    request += "\n"
                    request += "LOSE\n"

                    for i in range(len(self.players_roles_ID)):
                        if((self.players_roles_ID[i] != 1) and (self.players_roles_ID[i] != 4)):
                            request += str(self.players_ID[i]) + ", "
                    request = request[:-2]

                    asyncio.get_event_loop().run_until_complete(self.Send_all(request))

            # Есть ли в игре "Большой Змей"?
            if(self.vulture_sam_player_ID != -1): # Да
                cursor.execute(self.DB.send_all_cards_to_player.format(player_ID_from = str(player_ID), player_ID_to = str(self.vulture_sam_player_ID)))

                cards_ID = []
                for row in cursor:
                    cards_ID.append(str(row[0]))
                cursor.commit()

                request = "USE CHARACTER\n"
                request += "15\n"
                request += str(self.vulture_sam_player_ID) + "\n"
                request += "GET ALL CARDS FROM PLAYER\n"
                request += str(player_ID) + "\n"
                for i in range(len(cards_ID)):
                    request += str(cards_ID[i]) + ", "
                request = request[:-2]

                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            else: # Нет
                cursor.execute(self.DB.lose_all_cards.format(player_ID = str(player_ID), room_ID = str(self.room_ID)))

                cards_ID = []
                for row in cursor:
                    cards_ID.append(str(row[0]))
                cursor.commit()

                request = "LOSE ALL CARDS\n"
                request += str(player_ID) + "\n"
                for i in range(len(cards_ID)):
                    request += str(cards_ID[i]) + ", "
                request = request[:-2]

                asyncio.get_event_loop().run_until_complete(self.Send_all(request))

            # Какая роль убитого игрока?
            if(self.players_roles_ID[self.Get_i(player_ID)] == 2):
                if(killer_ID != ""):
                    request = "GET 3 CARDS\n"
                    request += str(player_ID) + "\n"

                    for i in range(3):
                        cursor.execute(self.DB.set_card_to_player_from_Deck.format(player_ID = str(player_ID), room_ID = str(self.room_ID)))
                        card_ID = cursor.fetchall()[0][0]
                        cursor.commit()

                        request += str(card_ID) + ", "
                    request = request[:-2]

                    await websocket.send(request)
            elif(self.players_roles_ID[self.Get_i(player_ID)] == 4):
                if((killer_ID == "1")):
                    cursor.execute(self.DB.lose_all_cards.format(player_ID = str(killer_ID), room_ID = str(self.room_ID)))

                    cards_ID = []
                    for row in cursor:
                        cards_ID.append(str(row[0]))
                    cursor.commit()

                    request = "LOSE ALL CARDS\n"
                    request += str(killer_ID) + "\n"
                    for i in range(len(cards_ID)):
                        request += str(cards_ID[i]) + ", "
                    request = request[:-2]

                    asyncio.get_event_loop().run_until_complete(self.Send_all(request))

        return code

    # Установка оружия
    async def Set_weapon(self, player_ID, name, firing_range, endless_bang, card_ID, message):
        cursor = self.conn.cursor()
        cursor.execute(self.DB.set_weapon.format(player_ID = str(player_ID), name = name, base_weapon = 0, firing_range = firing_range, endless_bang = endless_bang, weapon_card_ID = str(card_ID), room_ID = str(self.room_ID)))
        cursor.commit()

        cursor.execute(self.DB.change_card_location.format(card_ID = str(card_ID), card_location = '4'))
        cursor.commit()

        asyncio.get_event_loop().run_until_complete(self.Send_all(message))

    # Основной метод класса. Осуществляет приём и обмен сообщениями между участниками комнаты
    async def Data_exchange(self, websocket, path):
        try:
            self.conn = pyodbc.connect(self.DB.connection_string)
            cursor = self.conn.cursor()

            message = await websocket.recv()
            message_split = message.split('\n')

            print(message)
            print()

            # Предыгровые команды
            # Присоединение пользователя к комнате
            if(message_split[0] == "HELLO"):
                # Если комната не полная, то принимаем подключение
                if((self.count_of_players >= 0) and (self.count_of_players < self.max_count_of_players)):
                    mail = message_split[1]
                    password = message_split[2]
                    ip_address = message_split[3]
                    port = message_split[4]
                    self.players_IP.append(ip_address)
                    self.players_port.append(port)
                    print("IP address = ", ip_address)
                    print("port = ", port)

                    #print(self.DB.add_player_to_room.format(mail = mail, password = password, room_ID = str(self.room_ID)))
                    #print()
                    cursor.execute(self.DB.add_player_to_room.format(mail = mail, password = password, room_ID = str(self.room_ID)))

                    for row in cursor:
                        count_of_players = str(row[0])
                        max_count_of_players = str(row[1])
                    cursor.commit()

                    #print(self.DB.get_player_ID.format(mail = mail, password = password))
                    cursor.execute(self.DB.get_player_ID.format(mail = mail, password = password))

                    player_ID = ""
                    for row in cursor:
                        player_ID = str(row[0])

                    self.players_ID.append(player_ID)
                    self.players_status.append(False)

                    self.players_characters_ID.append(-1)
                    self.players_roles_ID.append(-1)

                    self.count_of_players = self.count_of_players + 1

                    request = self.requests.hello.format(count_of_players = count_of_players, max_count_of_players = max_count_of_players, player_ID = player_ID)
                    print(request)
                    print()
                    await websocket.send(request)

                    request = self.requests.new_player.format(count_of_players = count_of_players)
                    print(request)
                    #asyncio.get_event_loop().run_until_complete(self.Send_all_except_one(request, player_ID))
                    #asyncio.get_event_loop().run_until_complete(self.Send(request, 0, player_ID))
                    self.Send(request, 0, player_ID)
                # Если комната полная, то отклоняем подключение
                elif(self.count_of_players == self.max_count_of_players):
                    await websocket.send("FORBIDDEN 1")
                else:
                    await websocket.send("FORBIDDEN 2")
            # Изменение статуса готовности игрока (без запроса в БД)
            elif(message_split[0] == "SET READY"):
                player_ID = message_split[2]
                if(message_split[1] == "TRUE"):
                    self.players_status[self.Get_i(player_ID)] = True
                elif(message_split[1] == "FALSE"):
                    self.players_status[self.Get_i(player_ID)] = False
                print("0 OK")
                await websocket.send("0 OK")
                asyncio.get_event_loop().run_until_complete(self.Send_all_except_one(message, player_ID))
            # Начало стадии планирования
            elif(message_split[0] == "START PLANNING STAGE"):
                # Проверка подтверждения готовности всех игроков
                all_players_ready = True
                for i in range(len(self.players_status)):
                    if(not self.players_status[i]):
                        all_players_ready = False
                        break

                if(all_players_ready):
                    asyncio.get_event_loop().run_until_complete(self.Send_all(self.requests.planning))

                    # "Обнуление статусов всех игроков"
                    for i in range(len(self.players_status)):
                        self.players_status.append(i + 1)
                    

                # Запрос на получение max_count_of_players случайных персонажей
                cursor.execute(self.DB.getting_characters.format(n = str(self.max_count_of_players)))

                for row in cursor:
                    self.players_characters_ID.append(str(row[0]))

                cursor.commit()
                # Получение max_count_of_players случайных ролей (по правилам выдачи ролей)
                # 1 - шериф, 2 - бандит, 3 - ренегат, 4 - помощник
                self.players_roles_ID.append(1)
                self.players_roles_ID.append(2)
                self.players_roles_ID.append(2)
                self.players_roles_ID.append(3)
                if(self.max_count_of_players >= 5):
                    self.players_roles_ID.append(4)
                if(self.max_count_of_players >= 6):
                    self.players_roles_ID.append(2)
                if(self.max_count_of_players == 7):
                    self.players_roles_ID.append(4)
                random.shuffle(self.players_roles_ID)

                # Генерация порядкового номера для каждого игрока
                for i in range(self.max_count_of_players):
                    self.players_queue.append(i + 1)
                    self.players_alive.append(1)
                random.shuffle(self.players_queue)
            # Запрос на получение персонажа
            elif(message_split[0] == "GET CHARACTER"):
                player_ID = message_split[1]
                
                if(str(self.players_characters_ID[self.Get_i(int(player_ID))]) == "15"):
                    self.vulture_sam_player_ID = player_ID

                cursor.execute(self.DB.add_character_to_player.format(player_ID = player_ID, characters_ID = str(self.players_characters_ID[self.Get_i(int(player_ID))])))
                code = cursor.fetchall()[0][0]
                cursor.commit()

                if(str(code) == "0"):
                    request = "SET CHARACTER\n"
                    request += self.players_characters_ID[self.Get_i(int(player_ID))]

                    await websocket.send(request)
                else:
                    await websocket.send("-1")
            # Запрос на получение роли
            elif(message_split[0] == "GET ROLE"):
                player_ID = message_split[1]

                cursor.execute(self.DB.add_role_to_player.format(player_ID = player_ID, roles_ID = str(self.players_roles_ID[self.Get_i(int(player_ID))])))
                code = cursor.fetchall()[0][0]
                cursor.commit()

                if(str(code) == "0"):
                    request = "SET ROLE\n"
                    request += str(self.players_roles_ID[self.Get_i(int(player_ID))])

                    await websocket.send(request)
                else:
                    await websocket.send("-1")
            # Приём подтверждение готовности игрока к передаче данных о других игроках (без запроса в БД)
            elif(message_split[0] == "CHARACTER AND ROLE SELECTED"):
                # Изменение статуса игрока
                player_ID = message_split[1]
                self.players_status[self.Get_i(player_ID)] = True

                await websocket.send("0 OK")
            # Приём запроса на отправку данных о других игроках (без запроса в БД)
            elif(message_split[0] == "GET PLAYERS INFO"):
                player_ID = message_split[1]

                request = str(self.players_queue[self.Get_i(player_ID)]) + "\n"
                for i in range(len(self.players_ID)):
                    request += str(i + 1) + ", " + str(self.players_ID[i]) + ", " + str(self.players_characters_ID[i]) + "\n"
                request = request[:-1]
                print("request =\n", request)

                await websocket.send(request)
            # Приём запроса на получение стартовых карт
            elif(message_split[0] == "GET START CARDS"):
                player_ID = message_split[1]

                cursor.execute(self.DB.get_max_lives.format(player_ID = player_ID))

                max_lives = str(cursor.fetchall()[0][0])
                request = "SET START CARDS\n"

                for i in range(int(max_lives)):
                    cursor.execute(self.DB.set_card_to_player_from_Deck.format(player_ID = player_ID, room_ID = str(self.room_ID)))
                    card_ID = cursor.fetchall()[0][0]
                    cursor.commit()

                    request += str(card_ID) + "\n"

                request = request[:-1]

                await websocket.send(request)
            # Приём подтверждения готовности к началу игры (без запроса в БД)
            elif(message_split[0] == "START GAME"):
                player_ID = message_split[1]
                self.players_status[self.Get_i(player_ID)] = True

                all_is_ready = True
                for i in range(len(self.players_status)):
                    if(not self.players_status[i]):
                        all_is_ready = False
                        break

                if(all_is_ready):
                    self.count_of_alive = self.max_count_of_players

                    self.current_queue = 1
                    self.current_i_queue = self.Get_i_queue(self.current_queue)

                    request = "GAME IS START\n"
                    request += "SET MOVE\n"
                    request += self.players_ID[self.current_i_queue]
                    asyncio.get_event_loop().run_until_complete(self.Send_all(request))

            # Игровые команды
            # Вспомогательные команды
            # Получение сообщения об окончании хода (без запроса в БД)
            elif(message_split[0] == "SET MOVE END"):
                player_ID = message_split[1]

                request = "SET MOVE\n"

                if(self.current_queue + 1 <= self.max_count_of_players):
                    self.current_queue = self.current_queue + 1
                else:
                    self.current_queue = 1

                self.current_i_queue = self.Get_i_queue(self.current_queue)
                request += str(self.players_ID[self.current_i_queue])
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))

            # Розыгрыш карт
            
            # Проверка, есть ли карта у игрока

            # Розыгрыш карты "Бэнг"
            elif(message_split[0] == "PLAY BANG"):
                player_ID = message_split[1].split(', ')[0]
                player_ID = message_split[1].split(', ')[1]
                card_ID = message_split[2]

                # Проверка, может ли игрок выстрелить

                self.cards_ID_to_dropping.append(int(card_ID))

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Розыгрыш карты "Мимо"
            elif(message_split[0] == "PLAY MISSED"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                self.Play_missed(message, player_ID, card_ID, message_split)
            # Розыгрыш 2-ух карт "Мимо"
            elif(message_split[0] == "PLAY 2 MISSED"):
                card_ID_1 = message_split[2].split(', ')[0]
                card_ID_2 = message_split[2].split(', ')[1]

                self.Send_card_to_Dropping(int(card_ID_1))
                self.Send_card_to_Dropping(int(card_ID_2))
                self.Cards_to_Dropping()

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Розыгрыш карты "Пиво"
            elif(message_split[0] == "PLAY BEER"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                # Проверка, может ли игрок сыграть карту "Пиво" (не максимальное ли количество жизней у игрока)

                cursor.execute(self.DB.recovery_health.format(player_ID = str(player_ID)))
                cursor.commit()

                self.Send_card_to_Dropping(int(card_ID))

                request = message
                request += "\n"
                request += "GET 1 HP"
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Розыгрыш карты "Дуэль"
            elif(message_split[0] == "PLAY DUEL"):
                player_ID = message_split[1].split(', ')[0]
                player_ID = message_split[1].split(', ')[1]
                card_ID = message_split[2]

                self.cards_ID_to_dropping.append(int(card_ID))

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Использование карты "Бэнг" для карт "Дуэль", "Индейцы"
            elif(message_split[0] == "USE BANG"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                self.Send_card_to_Dropping(int(card_ID))

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))

                if(len(message_split) > 3):
                    if((message_split[3] == "PLAY INDIANS") and (self.counter_helper + 1 < self.count_of_alive)):
                        self.counter_helper = self.counter_helper + 1

                        while(true):
                            if(self.current_queue + 1 <= self.max_count_of_players):
                                self.current_queue_helper = self.current_queue + 1
                            else:
                                self.current_queue_helper = 1
                            self.current_i_queue_helper = self.Get_i_queue(self.current_queue_helper)
                            if(self.players_alive[self.current_i_queue_helper] == 1):
                                break

                        request = "PLAY INDIANS\n"
                        request += str(player_ID) + ", " + str(self.players_ID[self.current_i_queue_helper]) + "\n"
                        request += str(self.cards_ID_to_dropping[0])
                        asyncio.get_event_loop().run_until_complete(self.Send_all(request))
                    elif((message_split[3] == "PLAY INDIANS") and (self.counter_helper + 1 == self.count_of_alive)):
                        self.Cards_to_Dropping()

                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Розыгрыш карты "Паника"
            elif(message_split[0] == "PLAY PANIC"):
                player_ID = message_split[1].split(', ')[0]
                player_ID = message_split[1].split(', ')[1]
                card_ID = message_split[2]

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))

                if(message_split[3] == "STEAL 1 CARD FROM FIELD"):
                    target_card_ID = message_split[4]

                    cursor = self.conn.cursor()
                    cursor.execute(self.DB.stealing_card_from_player.format(player_ID_to = str(player_ID), card_ID = str(target_card_ID)))
                    cursor.commit()

                    if((str(card_name) == "volcanic") or (str(card_name) == "schofield") or (str(card_name) == "remington") or (str(card_name) == "rev_carabine") or (str(card_name) == "winchester")):
                        sql = self.DB.set_weapon.format(player_ID = str(player_ID), name = 'colt', base_weapon = 1, firing_range = 1, endless_bang = 0, weapon_card_ID = 'NULL', room_ID = str(self.room_ID))
                    elif(str(card_name) == "mustang"):
                        sql = self.DB.change_additional_defence_range.format(player_ID = str(player_ID), n = str(-1))
                    elif(str(card_name) == "scope"):
                        sql = self.DB.change_additional_attack_range.format(player_ID = str(player_ID), n = str(-1))

                    cursor.execute(sql)
                    cursor.commit()
                elif(message_split[3] == "STEAL 1 CARD FROM HAND"):
                    self.Steal_card_from_hand(player_ID, player_ID)

                self.Send_card_to_Dropping(int(card_ID))
            # Розыгрыш карты "Красотка"
            elif(message_split[0] == "PLAY CAT BALOU"):
                player_ID = message_split[1].split(', ')[0]
                player_ID = message_split[1].split(', ')[1]
                card_ID = message_split[2]

                if(message_split[3] == "DISCARD 1 CARD FROM FIELD"):
                    target_card_ID = message_split[4]

                    self.Send_card_to_Dropping(int(target_card_ID))

                    cursor = self.conn.cursor()
                    cursor.execute(self.DB.get_card_name.format(card_ID = str(target_card_ID)))
                    card_name = cursor.fetchall()[0][0]

                    if((str(card_name) == "volcanic") or (str(card_name) == "schofield") or (str(card_name) == "remington") or (str(card_name) == "rev_carabine") or (str(card_name) == "winchester")):
                        sql = self.DB.set_weapon.format(player_ID = str(player_ID), name = 'colt', base_weapon = 1, firing_range = 1, endless_bang = 0, weapon_card_ID = 'NULL', room_ID = str(self.room_ID))
                    elif(str(card_name) == "mustang"):
                        sql = self.DB.change_additional_defence_range.format(player_ID = str(player_ID), n = str(-1))
                    elif(str(card_name) == "scope"):
                        sql = self.DB.change_additional_attack_range.format(player_ID = str(player_ID), n = str(-1))

                    cursor.execute(sql)
                    cursor.commit()

                    request = message
                    asyncio.get_event_loop().run_until_complete(self.Send_all(request))
                elif(message_split[3] == "DISCARD 1 CARD FROM HAND"):
                    cursor.execute(self.DB.get_player_cards.format(player_ID = str(player_ID)))

                    cards_ID = []
                    for row in cursor:
                        cards_ID.append(str(row[0]))

                    target_card_ID = cards_ID[math.floor(random.random() * len(cards_ID))]
                    self.cards_ID_to_dropping.append(int(target_card_ID))

                    request = message
                    request += "\n"
                    request += str(target_card_ID)
                    asyncio.get_event_loop().run_until_complete(self.Send_all(request))

                self.Send_card_to_Dropping(int(card_ID))
            # Розыгрыш карты "Волканик"
            elif(message_split[0] == "PLAY VOLCANIC"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                self.Set_weapon(player_ID, 'volcanic', 1, 1, card_ID, message)
            # Розыгрыш карты "Скофилд"
            elif(message_split[0] == "PLAY SCHOFIELD"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                self.Set_weapon(player_ID, 'schofield', 2, 0, card_ID, message)
            # Розыгрыш карты "Ремингтон"
            elif(message_split[0] == "PLAY REMINGTON"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                self.Set_weapon(player_ID, 'remington', 3, 0, card_ID, message)
            # Розыгрыш карты "Карабин"
            elif(message_split[0] == "PLAY REV CARABINE"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                self.Set_weapon(player_ID, 'rev_carabine', 4, 0, card_ID, message)
            # Розыгрыш карты "Винчестер"
            elif(message_split[0] == "PLAY WINCHESTER"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                self.Set_weapon(player_ID, 'winchester', 5, 0, card_ID, message)
            # Розыгрыш карты "Бочка"
            elif(message_split[0] == "PLAY BARREL"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                # Проверка, выложена ли на столе у игрока карта "Бочка"

                cursor.execute(self.DB.change_card_location.format(card_ID = str(card_ID), card_location = 4))
                cursor.commit()

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Проверка карты "Бочка" при выстреле
            elif(message_split[0] == "CHECK BARREL"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                self.Check_hit(message, player_ID)
            # Розыгрыш карты "Уэлс фарго"
            elif(message_split[0] == "PLAY WELLS FARGO"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))

                request = "GET 3 CARDS\n"
                request += str(player_ID) + "\n"

                for i in range(3):
                    cursor.execute(self.DB.set_card_to_player_from_Deck.format(player_ID = str(player_ID), room_ID = str(self.room_ID)))
                    card_ID = cursor.fetchall()[0][0]
                    cursor.commit()

                    request += str(card_ID) + ", "
                request = request[:-2]

                self.Send_card_to_Dropping(int(card_ID))

                await websocket.send(request)
            # Розыгрыш карты "Дилижанс"
            elif(message_split[0] == "PLAY STAGECOACH"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))

                request = "GET 2 CARDS\n"
                request += str(player_ID) + "\n"

                for i in range(2):
                    cursor.execute(self.DB.set_card_to_player_from_Deck.format(player_ID = str(player_ID), room_ID = str(self.room_ID)))
                    card_ID = cursor.fetchall()[0][0]
                    cursor.commit()

                    request += str(card_ID) + ", "
                request = request[:-2]

                self.Send_card_to_Dropping(int(card_ID))

                await websocket.send(request)
            # Розыгрыш карты "Мустанг"
            elif(message_split[0] == "PLAY MUSTANG"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                # Проверка, есть ли у игрока на столе карта "Мустанг"

                cursor.execute(self.DB.change_additional_defence_range.format(player_ID = str(player_ID), n = 1))
                cursor.commit()

                cursor.execute(self.DB.change_card_location.format(card_ID = str(card_ID), card_location = 4))
                cursor.commit()

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Розыгрыш карты "Тюрьма"
            elif(message_split[0] == "PLAY JAIL"):
                player_ID = message_split[1].split(', ')[0]
                player_ID = message_split[1].split(', ')[1]
                card_ID = message_split[2]

                cursor.execute(self.DB.Passing_card_to_player.format(player_ID = str(player_ID), card_ID = str(card_ID), card_location = 4))
                cursor.commit()

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Проверка карты "Тюрьма перед началом хода"
            elif(message_split[0] == "CHECK JAIL"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                cursor.execute(self.DB.get_card_for_checking.format(room_ID = str(self.room_ID)))

                request = message + "\n"
                check_card_ID = -1
                suit = ""
                for row in cursor:
                    check_card_ID = int(row[0])
                    suit = str(row[2])
                cursor.commit()

                if(suit == "H"):
                    request += "CHECK SUCCESS\n"
                else:
                    request += "CHECK FAIL\n"
                request += str(check_card_ID)
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))

                if(suit != "H"):
                    request = "SET MOVE\n"
                    if(self.current_queue + 1 <= self.max_count_of_players):
                        self.current_queue = self.current_queue + 1
                    else:
                        self.current_queue = 1

                    self.current_i_queue = self.Get_i_queue(self.current_queue)
                    request += str(self.players_ID[self.current_i_queue])

                    asyncio.get_event_loop().run_until_complete(self.Send_all(request))

                self.Send_card_to_Dropping(int(card_ID))
            # Розыгрыш карты "Индейцы"
            elif(message_split[0] == "PLAY INDIANS"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                self.counter_helper = 1
                self.current_queue_helper = -1
                
                while(true):
                    if(self.current_queue + 1 <= self.max_count_of_players):
                        self.current_queue_helper = self.current_queue + 1
                    else:
                        self.current_queue_helper = 1
                    self.current_i_queue_helper = self.Get_i_queue(self.current_queue_helper)
                    if(self.players_alive[self.current_i_queue_helper] == 1):
                        break

                request = "PLAY INDIANS\n"
                request += str(player_ID) + ", " + str(self.players_ID[self.current_i_queue_helper]) + "\n"
                request += str(card_ID)
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))

                self.cards_ID_to_dropping.append(int(card_ID))
            # Розыгрыш карты "Гатлинг"
            elif(message_split[0] == "PLAY GATLING"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                self.counter_helper = 1
                self.current_queue_helper = -1
                
                while(true):
                    if(self.current_queue + 1 <= self.max_count_of_players):
                        self.current_queue_helper = self.current_queue + 1
                    else:
                        self.current_queue_helper = 1
                    self.current_i_queue_helper = self.Get_i_queue(self.current_queue_helper)
                    if(self.players_alive[self.current_i_queue_helper] == 1):
                        break

                request = "PLAY GATLING\n"
                request += str(player_ID) + ", " + str(self.players_ID[self.current_i_queue_helper]) + "\n"
                request += str(card_ID)
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))

                self.cards_ID_to_dropping.append(int(card_ID))
            # Розыгрыш карты "Динамит"
            elif(message_split[0] == "PLAY DYNAMITE"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                # Проверка, выложена ли на столе у игрока карта "Динамит"

                cursor.execute(self.DB.change_card_location.format(card_ID = str(card_ID), card_location = 4))
                cursor.commit()

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Проверка динамита в начале хода
            elif(message_split[0] == "CHECK DYNAMITE"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                result, check_card_ID = self.Checking(["H", "K", "D"], ["10", "J", "Q", "K", "A"])

                if(result):
                    request += "CHECK FAIL\n"
                    request += str(check_card_ID) + "\n"
                    request += "LOSE 3 HP"
                    asyncio.get_event_loop().run_until_complete(self.Send_all(request))

                    killer_ID = ""
                    for i in range(3):
                        code = self.Lose_health(websocket, player_ID, "", message)
                        if(code == "10"):
                            break
                else:
                    request += "CHECK SUCCESS\n"
                    request += str(check_card_ID)
                    asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Розыгрыш карты "Магазин"
            elif(message_split[0] == "PLAY GENERAL STORE"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                cards_ID = []
                for i in range(self.count_of_alive):
                    cursor.execute(self.DB.set_cards_to_selection_stage.format(room_ID = str(self.room_ID)))
                    cards_ID.append(str(cursor.fetchall()[0][0]))
                    cursor.commit()

                request = message
                request += "\n"
                for i in range(len(cards_ID)):
                    request += str(cards_ID[i]) + ", "
                request = request[:-2]

                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Выбор игроком карты из магазина
            elif(message_split[0] == "CHOOSE 1 CARD FROM GENERAL STORE"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                cursor.execute(self.DB.passing_card_to_player.format(player_ID = str(player_ID), card_ID = str(card_ID), card_location = 3))
                cursor.commit()

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Розыгрыш карты "Салун"
            elif(message_split[0] == "PLAY SALOON"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                cursor.execute(self.DB.recovery_health_all_players.format(room_ID = str(self.room_ID)))

                recovery_HP_players_ID = []
                for row in cursor:
                    recovery_HP_players_ID.append(str(row[0]))
                cursor.commit()

                request = message
                request += "\n"
                request += "GET 1 HP\n"
                if(len(recovery_HP_players_ID) == 0):
                    request += "NOBODY"
                else:
                    for i in range(len(recovery_HP_players_ID)):
                        request += str(recovery_HP_players_ID[i]) + ", "
                    request = request[:-2]

                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Розыгрыш карты "Прицел"
            elif(message_split[0] == "PLAY SCOPE"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                # Проверка, выложена ли на столе у игрока карта "Прицел"

                cursor.execute(self.DB.change_additional_attack_range.format(player_ID = str(player_ID), n = 1))
                cursor.commit()

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))

            # Использование свойств персонажей
            elif(message_split[0] == "USE CHARACTER"):
                character_ID = message_split[1]
                player_ID = message_split[2]

                # Если используется свойство персонажа "Счастливчик Люк"
                if(character_ID == str(self.dict_characters["lucky_duke"])):
                    self.Check_hit(message, player_ID, card_ID)
                # Если используется свойство персонажа "Неуловимый Джо"
                elif(character_ID == str(self.dict_characters["paul_regret"])):
                    cursor.execute(self.DB.change_additional_defence_range.format(player_ID = str(player_ID), n = 1))
                    cursor.commit()
                
                    request = "0 OK"
                    await websocket.send(request)
                # Если используется свойство персонажа "Малыш Билли"
                elif(character_ID == str(self.dict_characters["willy_the_kid"])):
                    player_ID = message_split[4].split(', ')[0]
                    player_ID = message_split[4].split(', ')[1]
                    card_ID = message_split[5]

                    # Проверка, может ли игрок выстрелить

                    self.cards_ID_to_dropping.append(int(card_ID))

                    request = message
                    asyncio.get_event_loop().run_until_complete(self.Send_all(request))
                # Если используется свойство персонажа "Туко"
                elif(character_ID == str(self.dict_characters["pedro_ramires"])):
                    request = message
                    asyncio.get_event_loop().run_until_complete(self.Send_all_except_one(request, player_ID))

                    dropping_card_ID = self.Set_card_to_player_from_Dropping(player_ID)

                    cursor.execute(self.DB.set_card_to_player_from_Deck.format(player_ID = str(player_ID), room_ID = str(self.room_ID)))
                    deck_card_ID = str(cursor.fetchall()[0][0])
                    cursor.commit()

                    request = "GET 1 CARD CLOSED FROM DROPPING\n"
                    request += str(dropping_card_ID) + "\n"
                    request += "GET 1 CARD CLOSED FROM DECK\n"
                    request += str(deck_card_ID)

                    await websocket.send(request)
                # Если используется свойство персонажа "Кит Карсон"
                elif(character_ID == str(self.dict_characters["kit_carison"])):
                    request = message
                    asyncio.get_event_loop().run_until_complete(self.Send_all(request))

                    cards_ID = []
                    for i in range(3):
                        cursor.execute(self.DB.set_card_to_player_from_Deck.format(player_ID = str(player_ID), room_ID = str(self.room_ID)))
                        cards_ID.append(str(cursor.fetchall()[0][0]))
                        cursor.commit()

                    request = "GET 3 CARD CLOSED FROM DECK\n"
                    request += str(cards_ID[0]) + ", " + str(cards_ID[1]) + ", " + str(cards_ID[2])

                    await websocket.send(request)
                # Если используется свойство персонажа "Джанго"
                elif(character_ID == str(self.dict_characters["el_gringo"])):
                    player_ID = message_split[4]

                    request = message
                    asyncio.get_event_loop().run_until_complete(self.Send_all(request))

                    self.Steal_card_from_hand(player_ID, player_ID)
                # Если используется свойство персонажа "Джесси Джеймс"
                elif(character_ID == str(self.dict_characters["jesse_jones"])):
                    player_ID = message_split[4]

                    request = message
                    asyncio.get_event_loop().run_until_complete(self.Send_all(request))

                    self.Steal_card_from_hand(player_ID, player_ID)
                # Если используется свойство персонажа "Хладнокровная Рози"
                elif(character_ID == str(self.dict_characters["rose_doolan"])):
                    cursor.execute(self.DB.Change_additional_attack_range.format(player_ID = str(player_ID), n = 1))
                    cursor.commit()

                    request = "0 OK"
                    await websocket.send(request)
                # Если используется свойство персонажа "Человек-без-имени"
                elif(character_ID == str(self.dict_characters["jourdonnais"])):
                    self.Check_hit(message, player_ID)
                # Если используется свойство персонажа "Бедовая Джейн"
                elif(character_ID == str(self.dict_characters["calamity_janet"])):
                    if(message_split[3] == "PLAY MISSED LIKE BANG"):
                        card_ID = message_split[5]
                        self.cards_ID_to_dropping.append(int(card_ID))

                        request = message
                        asyncio.get_event_loop().run_until_complete(self.Send_all(request))
                    elif(message_split[3] == "PLAY BANG LIKE MISSED"):
                        self.Play_missed(message, player_ID, card_ID, message_split)
                # Если используется свойство персонажа "Сюзи Лафайет"
                elif(character_ID == str(self.dict_characters["suzy_lafayette"])):
                    request = message
                    asyncio.get_event_loop().run_until_complete(self.Send_all_except_one(request, player_ID))

                    self.Get_card_from_Deck(player_ID, websocket)
                # Если используется свойство персонажа "Бешеный Пёс"
                elif(character_ID == str(self.dict_characters["black_jack"])):
                    cursor.execute(self.DB.set_card_to_player_from_Deck.format(player_ID = str(player_ID), room_ID = str(self.room_ID)))
                    card_ID_1 = str(cursor.fetchall()[0][0])
                    cursor.commit()

                    result, check_card_ID = self.Checking(["H", "D"], [])

                    request = message + "\n"
                    if(result):
                        request += "CHECK SUCCESS\n"
                    else:
                        request += "CHECK FAIL\n"
                    request += str(check_card_ID)
                    asyncio.get_event_loop().run_until_complete(self.Send_all(request))

                    card_ID_2 = self.Set_card_to_player_from_Dropping(player_ID)

                    if(result):
                        cursor.execute(self.DB.Set_card_to_player_from_Deck.format(player_ID = str(player_ID), room_ID = str(self.room_ID)))
                        card_ID_3 = str(cursor.fetchall()[0][0])
                        cursor.commit()

                        request = "GET 3 CARDS FROM DECK\n"
                        request += str(card_ID_1) + ", " + str(card_ID_2) + ", " + str(card_ID_3)
                    else:
                        request = "GET 2 CARDS FROM DECK\n"
                        request += str(card_ID_1) + ", " + str(card_ID_2)

                    await websocket.send(request)
                # Если используется свойство персонажа "Том Кетчум"
                elif(character_ID == str(self.dict_characters["sid_ketchum"])):
                    card_ID_1 = message_split[0].split(', ')[0]
                    card_ID_2 = message_split[0].split(', ')[1]

                    # Проверка, не максимальное ли количество здоровья у игрока

                    cursor.execute(self.DB.recovery_health.format(player_ID = str(player_ID)))
                    cursor.commit()

                    self.Send_card_to_Dropping(int(card_ID_1))
                    self.Send_card_to_Dropping(int(card_ID_2))
                    
                    request = message
                    asyncio.get_event_loop().run_until_complete(self.Send_all(request))
                # Если используется свойство персонажа "Ангельские Глазки"
                elif(character_ID == str(self.dict_characters["slab_the_killer"])):
                    request = message
                    asyncio.get_event_loop().run_until_complete(self.Send_all(request))
                # Если используется свойство персонажа "Бутч Кесседи"
                elif(character_ID == str(self.dict_characters["bart_cassidy"])):
                    request = message
                    asyncio.get_event_loop().run_until_complete(self.Send_all(request))

                    self.Get_card_from_Deck(player_ID)

            # Вспомогательные команды
            # Потеря единицы здоровья игроком
            elif(message_split[0] == "LOSE 1 HP"):
                player_ID = ""
                killer_ID = ""
                if(len(message_split[1].split(', ')) > 1):
                    player_ID = message_split[1].split(', ')[0]
                    killer_ID = message_split[1].split(', ')[1]
                else:
                    player_ID = message_split[1]

                self.Lose_health(websocket, player_ID, killer_ID, message)
                self.Cards_to_Dropping()

                if(len(message_split) > 2):
                    if(message_split[2] == "PLAY INDIANS"):
                        self.counter_helper = self.counter_helper + 1

                        while(true):
                            if(self.current_queue + 1 <= self.max_count_of_players):
                                self.current_queue_helper = self.current_queue + 1
                            else:
                                self.current_queue_helper = 1
                            self.current_i_queue_helper = self.Get_i_queue(self.current_queue_helper)
                            if(self.players_alive[self.current_i_queue_helper] == 1):
                                break

                        request = "PLAY INDIANS\n"
                        request += str(player_ID) + ", " + str(self.players_ID[self.current_i_queue_helper]) + "\n"
                        request += str(self.cards_ID_to_dropping[0])
                        asyncio.get_event_loop().run_until_complete(self.Send_all(request))
                    elif((message_split[2] == "PLAY INDIANS") and (self.counter_helper + 1 == self.count_of_alive)):
                        self.Cards_to_Dropping()

                    if((message_split[2] == "PLAY GATLING") and (self.counter_helper + 1 < self.count_of_alive)):
                        self.counter_helper = self.counter_helper + 1

                        while(true):
                            if(self.current_queue + 1 <= self.max_count_of_players):
                                self.current_queue_helper = self.current_queue + 1
                            else:
                                self.current_queue_helper = 1
                            self.current_i_queue_helper = self.Get_i_queue(self.current_queue_helper)
                            if(self.players_alive[self.current_i_queue_helper] == 1):
                                break

                        request = "PLAY GATLING\n"
                        request += str(player_ID) + ", " + str(self.players_ID[self.current_i_queue_helper]) + "\n"
                        request += str(self.cards_ID_to_dropping[0])
                        asyncio.get_event_loop().run_until_complete(self.Send_all(request))
                    elif((message_split[2] == "PLAY GATLING") and (self.counter_helper + 1 == self.count_of_alive)):
                        self.Cards_to_Dropping()

                    asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Возвращение карты в колоду после использовании роли "Кит Карсон"
            elif(message_split[0] == "RETURN 1 CARD CLOSED ON DECK"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                request = "RETURN 1 CARD CLOSED ON DECK"
                request += str(player_ID)

                asyncio.get_event_loop().run_until_complete(self.Send_all(request))

                cursor.execute(self.DB.return_card_to_Deck.format(card_ID = str(card_ID), room_ID = str(self.room_ID)))
                cursor.commit()
            # Получить карту из колоды
            elif(message_split[0] == "GET 1 CARD CLOSED FROM DECK"):
                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all_except_one(request, player_ID))

                player_ID = message_split[1]

                self.Get_card_from_Deck(player_ID, websocket)
            # Получить 2 карты из колоды
            elif(message_split[0] == "GET 2 CARDS CLOSED FROM DECK"):
                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all_except_one(request, player_ID))

                player_ID = message_split[1]

                deck_cards_ID = []

                for i in range(2):
                    cursor.execute(self.DB.set_card_to_player_from_Deck.format(player_ID = str(player_ID), room_ID = str(self.room_ID)))
                    deck_cards_ID.append(str(cursor.fetchall()[0][0]))
                    cursor.commit()

                request = "GET 2 CARDS\n"
                request += str(deck_cards_ID[0]) + ", " + str(deck_cards_ID[1])

                await websocket.send(request)
        except(Exception) as e:
            await websocket.send('-1')
            print(e)
        else:
            cursor.commit()
        finally:
            print("---------------")
            self.conn.close()