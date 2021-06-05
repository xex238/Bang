import asyncio
import websockets
import random
import math

class Room:
    room_ID = -1 # ID комнаты (аналогичен значению в БД)
    room_status = "open" # Статус комнаты (аналогичен значению в БД)
    room_IP = None # IP адрес комнаты
    room_port = None # Порт комнаты

    server = None # Сервер комнаты

    max_count_of_players = -1 # Максимальное количество игроков в комнате
    count_of_players = 0 # Текущее количество игроков в комнате

    players_ID = [] # Список ID участников комнаты
    players_status = [] # Список статусов участников комнаты (для начала стадии планирования,
    # для начала передачи информации о других игроках после выбора персонажа и роли, для начала игры)
    players_IP = [] # Список IP адресов участников комнаты
    players_port = [] # Список портов участников комнаты

    players_roles_ID = [] # Список ID ролей участников комнаты
    players_characters_ID = [] # Список ID персонажей участников комнаты

    players_queue = [] # Очередь хода игрока (по часовой стрелке, начиная от шерифа, шериф имеет значение 1)
    player_ID_step = -1 # ID игрока, который ходит в данный момент

    count_of_cards_in_deck = 80 # Количество карт в колоде
    count_of_cards_in_dropping = 0 # Количество карт в сбросе

    cards_ID_to_dropping = [] # Список карт, которые необходимо будет отправить в сброс

    def __init__(self, max_count_of_players, room_ID, room_IP, room_port):
        self.max_count_of_players = max_count_of_players

        self.room_ID = room_ID
        self.room_status = "open"
        self.room_IP = room_IP
        self.room_port = room_port

    # Возвращение порядкового номера в массиве по ID
    def Get_i(self, player_ID):
        for i in range(len(self.players_ID)):
            if(self.players_ID[i] == player_ID):
                return i

    # Открытие (запуск) комнаты
    def Start_room(self):
        self.server = websockets.serve(self.Data_exchange, self.room_IP, self.room_port)
        asyncio.get_event_loop().run_until_complete(self.server)
        asyncio.get_event_loop().run_forever()

    # Отправка сообщения одному игроку
    async def Send(self, message, i):
        uri = "ws://" + self.room_IP[i] + ":" + self.room_port[i]
        async with websockets.connect(uri) as websocket:
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
            sql = "exec dbo.Send_card_to_Dropping\n"
            sql += "@card_ID = " + str(self.cards_ID_to_dropping[i]) + ",\n"
            sql += "@room_ID = " + str(self.room_ID)

            cursor = self.conn.cursor()
            cursor.execute(sql)
            cursor.commit()

        self.cards_ID_to_dropping.clear()

    # Основной метод класса. Осуществляет приём и обмен сообщениями между участниками комнаты
    async def Data_exchange(self, websocket, path):
        try:
            self.conn = pyodbc.connect(str(self.driver + self.server + self.database + self.user + self.password + self.TC))

            message = await websocket.recv()
            message_split = message.split('\n')

            # Предыгровые команды
            # Присоединение пользователя к комнате
            if(message_split[0] == "HELLO"):
                # Если комната не полная, то принимаем подключение
                if((self.count_of_players >= 0) and (self.count_of_players < self.max_count_of_players)):
                    mail = message_split[1]
                    password = message_split[2]

                    sql = "exec dbo.Add_player_to_room\n"
                    sql += "@mail = '" + mail + "',\n"
                    sql += "@password = '" + password + "',\n"
                    sql += "@room_ID = " + str(self.room_ID)

                    cursor = self.conn.cursor()
                    cursor.execute(sql)
                    cursor.commit()

                    request = "HELLO\n"

                    for row in cursor:
                        request += str(row[0]) + ", " + str(row[1]) + "\n"
                        print(row)
                        print()

                    sql = "exec dbo.Get_player_ID\n"
                    sql += "@mail = '" + mail + "',\n"
                    sql += "@password = '" + password + "'"

                    cursor.execute(sql)

                    player_ID = ""
                    for row in cursor:
                        player_ID = str(row[0])
                        request += str(row[0])
                        print(row)
                        print()

                    self.players_ID.append(player_ID)
                    self.players_status.append(False)
                    self.players_IP.append(websocket.remote_address[0])
                    self.players_port.append(websocket.remote_address[1])

                    self.players_characters_ID.append(-1)
                    self.players_roles_ID.append(-1)

                    self.count_of_players = self.count_of_players + 1
                    await websocket.send(request)

                    request = "NEW PLAYER\n"
                    request += count_of_players

                    asyncio.get_event_loop().run_until_complete(self.Send_all_except_one(request, player_ID))
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
                    asyncio.get_event_loop().run_until_complete(self.Send_all("PLANNING STAGE IS STARTING"))

                    # "Обнуление статусов всех игроков"
                    for i in range(len(self.players_status)):
                        self.players_status.append(i + 1)
                    

                # Запрос на получение max_count_of_players случайных персонажей
                sql = "exec dbo.Getting_characters\n"
                sql += "@n = " + str(self.max_count_of_players)

                cursor = self.conn.cursor()
                cursor.execute(sql)
                cursor.commit()

                for row in cursor:
                    self.players_characters_ID.append(str(row[0]))

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
                    self.players_queue[i] = i + 1
                random.shuffle(self.players_queue)
            # Запрос на получение персонажа
            elif(message_split[0] == "GET CHARACTER"):
                player_ID = message_split[1]
                
                sql = "exec dbo.Add_character_to_player\n"
                sql += "@player_ID = " + player_ID + ",\n"
                sql += "@characters_ID = " + str(self.players_characters_ID[self.Get_i(int(player_ID))])

                cursor = self.conn.cursor()
                cursor.execute(sql)
                cursor.commit()
                code = cursor.fetchall()[0][0]

                if(str(code) == "0"):
                    request = "SET CHARACTER\n"
                    request += self.players_characters_ID[self.Get_i(int(player_ID))]

                    await websocket.send(request)
                else:
                    await websocket.send("-1")
            # Запрос на получение роли
            elif(message_split[0] == "GET ROLE"):
                player_ID = message_split[1]

                sql = "exec dbo.Add_role_to_player\n"
                sql += "@player_ID = " + player_ID + ",\n"
                sql += "@roles_ID = " + str(self.players_roles_ID[self.Get_i(int(player_ID))])

                cursor = self.conn.cursor()
                cursor.execute(sql)
                cursor.commit()
                code = cursor.fetchall()[0][0]

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
                for i in range(len(self.players_ID) - 1):
                    request += str(i + 1) + ", " + str(self.players_ID[i]) + ", " + str(self.players_characters_ID[i]) + "\n"
                request += str(len(self.players_ID) - 1 + 1) + ", " + str(self.players_ID[len(self.players_ID) - 1]) + ", " + str(self.players_characters_ID[len(self.players_ID) - 1])
                print("request =\n", request)

                await websocket.send(request)
            # Приём запроса на получение стартовых карт
            elif(message_split[0] == "GET START CARDS"):
                player_ID = message_split[1]

                sql = "exec dbo.Get_max_lives\n"
                sql += "@player_ID = " + str(player_ID)

                cursor = self.conn.cursor()
                cursor.execute(sql)

                max_lives = str(cursor.fetchall()[0][0])
                request = "SET START CARDS\n"

                for i in range(int(max_lives)):
                    sql = "exec dbo.Set_card_to_player_from_Deck\n"
                    sql += "@player_ID = " + player_ID + ",\n"
                    sql += "@room_ID = " + str(self.room_ID)

                    cursor = self.conn.cursor()
                    cursor.execute(sql)
                    cursor.commit()

                    card_ID = cursor.fetchall()[0][0]
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
                    request = "GAME IS START\n"
                    request += "SET MOVE\n"
                    request += self.players_queue[0]
                    asyncio.get_event_loop().run_until_complete(self.Send_all(request))

            # Игровые команды
            # Вспомогательные команды
            # Получение сообщения об окончании хода (без запроса в БД)
            elif(message_split[0] == "SET MOVE END"):
                player_ID = message_split[1]
                request = "SET MOVE\n"
                if(player_ID + 1 < len(self.players_ID)):
                    request += self.players_ID[self.Get_i(player_ID) + 1]
                else:
                    request += self.players_ID[0]
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))

            # Розыгрыш карт
            
            # Проверка, есть ли карта у игрока

            # Розыгрыш карты "Бэнг"
            elif(message_split[0] == "PLAY BANG"):
                player_ID = message_split[1].split(', ')[0]
                target_ID = message_split[1].split(', ')[1]
                card_ID = message_split[2]

                # Проверка, может ли игрок выстрелить

                self.cards_ID_to_dropping.append(int(card_ID))

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Розыгры карты "Мимо"
            elif(message_split[0] == "PLAY MISSED"):
                target_ID = message_split[1]
                card_ID = message_split[2]

                self.cards_ID_to_dropping.append(int(card_ID))
                self.Cards_to_Dropping()

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Розыгрыш карты "Пиво"
            elif(message_split[0] == "PLAY BEER"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                # Проверка, может ли игрок сыграть карту "Пиво" (не максимальное ли количество жизней у игрока)

                self.cards_ID_to_dropping.append(int(card_ID))
                self.Cards_to_Dropping()

                request = message
                request += "\n"
                request += "GET 1 HP"
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Розыгрыш карты "Дуэль"
            elif(message_split[0] == "PLAY DUEL"):
                player_ID = message_split[1].split(', ')[0]
                target_ID = message_split[1].split(', ')[1]
                card_ID = message_split[2]

                self.cards_ID_to_dropping.append(int(card_ID))

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Использование карты "Бэнг" в рамках дуэли
            elif(message_split[0] == "USE BANG"):
                target_ID = message_split[1]
                card_ID = message_split[2]

                self.cards_ID_to_dropping.append(int(card_ID))

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Розыгрыш карты "Паника"
            elif(message_split[0] == "PLAY PANIC"):
                player_ID = message_split[1].split(', ')[0]
                target_ID = message_split[1].split(', ')[1]
                card_ID = message_split[2]

                if(message_split[3] == "STEAL 1 CARD FROM FIELD"):
                    target_card_ID = message_split[4]

                    sql = "exec dbo.Stealing_card_from_player\n"
                    sql += "@player_ID_to = " + str(player_ID) + ",\n"
                    sql += "@card_ID = " + str(target_card_ID)

                    cursor = self.conn.cursor()
                    cursor.execute(sql)
                    cursor.commit()

                    if((str(card_name) == "volcanic") or (str(card_name) == "schofield") or (str(card_name) == "remington") or (str(card_name) == "rev_carabine") or (str(card_name) == "winchester")):
                        sql = "exec dbo.Get_weapon\n"
                        sql += "@player_ID = " + str(target_ID) + ",\n"
                        sql += "@name = 'colt',\n"
                        sql += "@base_weapon = 1,\n"
                        sql += "@firing_range = 1,\n"
                        sql += "@endless_bang = 0"
                    elif(str(card_name) == "mustang"):
                        sql = "exec dbo.Change_additional_defence_range\n"
                        sql += "@player_ID = " + str(target_ID) + ",\n"
                        sql += "@n = -1"
                    elif(str(card_name) == "scope"):
                        sql = "exec dbo.Change_additional_attack_range\n"
                        sql += "@player_ID = " + str(target_ID) + ",\n"
                        sql += "@n = -1"

                    cursor = self.conn.cursor()
                    cursor.execute(sql)
                    cursor.commit()

                    request = message
                    asyncio.get_event_loop().run_until_complete(self.Send_all(request))
                elif(message_split[3] == "STEAL 1 CARD FROM HAND"):
                    sql = "exec dbo.Get_player_cards\n"
                    sql += "@player_ID = " + str(target_ID)

                    cursor = self.conn.cursor()
                    cursor.execute(sql)

                    cards_ID = []
                    for row in cursor:
                        cards_ID.append(str(row[0]))

                    target_card_ID = cards_ID[math.floor(random.random() * len(cards_ID))]

                    sql = "exec dbo.Stealing_card_from_player\n"
                    sql += "@player_ID_to = " + str(player_ID) + ",\n"
                    sql += "@card_ID = " + str(target_card_ID)

                    cursor = self.conn.cursor()
                    cursor.execute(sql)
                    cursor.commit()

                    request = message
                    asyncio.get_event_loop().run_until_complete(self.Send_all(request))

                    request = "LOSE 1 CARD\n"
                    request += str(target_card_ID)

                    asyncio.get_event_loop().run_until_complete(self.Send(request, self.Get_i(targer_ID)))

                    request = "GET 1 CARD"
                    request += str(target_card_ID)

                    await websocket.send(request)

                self.cards_ID_to_dropping.append(int(card_ID))
                self.Cards_to_Dropping()
            # Розыгрыш карты "Красотка"
            elif(message_split[0] == "PLAY CAT BALOU"):
                player_ID = message_split[1].split(', ')[0]
                target_ID = message_split[1].split(', ')[1]
                card_ID = message_split[2]

                if(message_split[3] == "DISCARD 1 CARD FROM FIELD"):
                    target_card_ID = message_split[4]

                    self.cards_ID_to_dropping.append(int(target_card_ID))

                    sql = "exec dbo.Get_card_name\n"
                    sql += "@card_ID = " + str(target_card_ID)

                    cursor = self.conn.cursor()
                    cursor.execute(sql)
                    card_name = cursor.fetchall()[0][0]

                    if((str(card_name) == "volcanic") or (str(card_name) == "schofield") or (str(card_name) == "remington") or (str(card_name) == "rev_carabine") or (str(card_name) == "winchester")):
                        sql = "exec dbo.Get_weapon\n"
                        sql += "@player_ID = " + str(target_ID) + ",\n"
                        sql += "@name = 'colt',\n"
                        sql += "@base_weapon = 1,\n"
                        sql += "@firing_range = 1,\n"
                        sql += "@endless_bang = 0"
                    elif(str(card_name) == "mustang"):
                        sql = "exec dbo.Change_additional_defence_range\n"
                        sql += "@player_ID = " + str(target_ID) + ",\n"
                        sql += "@n = -1"
                    elif(str(card_name) == "scope"):
                        sql = "exec dbo.Change_additional_attack_range\n"
                        sql += "@player_ID = " + str(target_ID) + ",\n"
                        sql += "@n = -1"

                    cursor = self.conn.cursor()
                    cursor.execute(sql)
                    cursor.commit()

                    request = message
                    asyncio.get_event_loop().run_until_complete(self.Send_all(request))
                elif(message_split[3] == "DISCARD 1 CARD FROM HAND"):
                    sql = "exec dbo.Get_player_cards\n"
                    sql += "@player_ID = " + str(target_ID)

                    cursor = self.conn.cursor()
                    cursor.execute(sql)

                    cards_ID = []
                    for row in cursor:
                        cards_ID.append(str(row[0]))

                    target_card_ID = cards_ID[math.floor(random.random() * len(cards_ID))]
                    self.cards_ID_to_dropping.append(int(target_card_ID))

                    request = message
                    request += "\n"
                    request += str(target_card_ID)
                    asyncio.get_event_loop().run_until_complete(self.Send_all(request))

                self.cards_ID_to_dropping.append(int(card_ID))
                self.Cards_to_Dropping()
            # Розыгрыш карты "Волканик"
            elif(message_split[0] == "PLAY VOLCANIC"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                sql = "exec dbo.Set_weapon\n"
                sql += "@player_ID = " + str(player_ID) + ",\n"
                sql += "@name = 'volcanic',\n"
                sql += "@base_weapon = 0,\n"
                sql += "@firing_range = 1,\n"
                sql += "@endless_bang = 1,\n"
                sql += "@weapon_card_ID = " + str(card_ID) + ",\n"
                sql += "@room_ID = " + str(self.room_ID)

                cursor = self.conn.cursor()
                cursor.execute(sql)
                cursor.commit()

                sql = "exec dbo.Change_card_location\n"
                sql += "@card_ID = " + str(card_ID) + ",\n"
                sql += "@card_location = 4"

                cursor = self.conn.cursor()
                cursor.execute(sql)
                cursor.commit()

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Розыгрыш карты "Скофилд"
            elif(message_split[0] == "PLAY SCHOFIELD"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                sql = "exec dbo.Set_weapon\n"
                sql += "@player_ID = " + str(player_ID) + ",\n"
                sql += "@name = 'volcanic',\n"
                sql += "@base_weapon = 0,\n"
                sql += "@firing_range = 2,\n"
                sql += "@endless_bang = 0,\n"
                sql += "@weapon_card_ID = " + str(card_ID) + ",\n"
                sql += "@room_ID = " + str(self.room_ID)

                cursor = self.conn.cursor()
                cursor.execute(sql)
                cursor.commit()

                sql = "exec dbo.Change_card_location\n"
                sql += "@card_ID = " + str(card_ID) + ",\n"
                sql += "@card_location = 4"

                cursor = self.conn.cursor()
                cursor.execute(sql)
                cursor.commit()

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Розыгрыш карты "Ремингтон"
            elif(message_split[0] == "PLAY REMINGTON"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                sql = "exec dbo.Get_weapon\n"
                sql += "@player_ID = " + str(player_ID) + ",\n"
                sql += "@name = 'remington',\n"
                sql += "@base_weapon = 0,\n"
                sql += "@firing_range = 3,\n"
                sql += "@endless_bang = 0,\n"
                sql += "@weapon_card_ID = " + str(card_ID) + ",\n"
                sql += "@room_ID = " + str(self.room_ID)

                cursor = self.conn.cursor()
                cursor.execute(sql)
                cursor.commit()

                sql = "exec dbo.Change_card_location\n"
                sql += "@card_ID = " + str(card_ID) + ",\n"
                sql += "@card_location = 4"

                cursor = self.conn.cursor()
                cursor.execute(sql)
                cursor.commit()

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Розыгрыш карты "Карабин"
            elif(message_split[0] == "PLAY REV CARABINE"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                sql = "exec dbo.Get_weapon\n"
                sql += "@player_ID = " + str(player_ID) + ",\n"
                sql += "@name = 'rev_carabine',\n"
                sql += "@base_weapon = 0,\n"
                sql += "@firing_range = 4,\n"
                sql += "@endless_bang = 0,\n"
                sql += "@weapon_card_ID = " + str(card_ID) + ",\n"
                sql += "@room_ID = " + str(self.room_ID)

                cursor = self.conn.cursor()
                cursor.execute(sql)
                cursor.commit()

                sql = "exec dbo.Change_card_location\n"
                sql += "@card_ID = " + str(card_ID) + ",\n"
                sql += "@card_location = 4"

                cursor = self.conn.cursor()
                cursor.execute(sql)
                cursor.commit()

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Розыгрыш карты "Винчестер"
            elif(message_split[0] == "PLAY WINCHESTER"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                sql = "exec dbo.Get_weapon\n"
                sql += "@player_ID = " + str(player_ID) + ",\n"
                sql += "@name = 'winchester',\n"
                sql += "@base_weapon = 0,\n"
                sql += "@firing_range = 5,\n"
                sql += "@endless_bang = 0,\n"
                sql += "@weapon_card_ID = " + str(card_ID) + ",\n"
                sql += "@room_ID = " + str(self.room_ID)

                cursor = self.conn.cursor()
                cursor.execute(sql)
                cursor.commit()

                sql = "exec dbo.Change_card_location\n"
                sql += "@card_ID = " + str(card_ID) + ",\n"
                sql += "@card_location = 4"

                cursor = self.conn.cursor()
                cursor.execute(sql)
                cursor.commit()

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Розыгрыш карты "Бочка"
            elif(message_split[0] == "PLAY BARREL"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                # Проверка, выложена ли на столе у игрока карта "Бочка"

                sql = "exec dbo.Change_card_location\n"
                sql += "@card_ID = " + str(card_ID) + ",\n"
                sql += "@card_location = 4"

                cursor = self.conn.cursor()
                cursor.execute(sql)
                cursor.commit()

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Проверка карты "Бочка" при выстреле
            elif(message_split[0] == "CHECK BARREL"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                sql = "exec dbo.Get_card_for_checking\n"
                sql += "@room_ID = " + str(self.room_ID)

                cursor = self.conn.cursor()
                cursor.execute(sql)
                cursor.commit()

                request = message + "\n"
                check_card_ID = -1
                suit = ""
                for row in cursor:
                    check_card_ID = int(row[0])
                    suit = str(row[2])

                if(suit == "H"):
                    request += "CHECK SUCCESS\n"
                else:
                    request += "CHECK FAIL\n"
                request += str(check_card_ID)
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Розыгрыш карты "Уэлс фарго"
            elif(message_split[0] == "PLAY WELLS FARGO"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))

                request = "GET 3 CARDS\n"
                request += str(player_ID) + "\n"

                for i in range(3):
                    sql = "exec dbo.Set_card_to_player_from_Deck\n"
                    sql += "@player_ID = " + str(player_ID) + ",\n"
                    sql += "@room_ID = " + str(self.room_ID)

                    cursor = self.conn.cursor()
                    cursor.execute(sql)
                    cursor.commit()

                    card_ID = cursor.fetchall()[0][0]
                    request += str(card_ID) + ", "
                request = request[:-2]

                self.cards_ID_to_dropping.append(int(card_ID))
                self.Cards_to_Dropping()

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
                    sql = "exec dbo.Set_card_to_player_from_Deck\n"
                    sql += "@player_ID = " + str(player_ID) + ",\n"
                    sql += "@room_ID = " + str(self.room_ID)

                    cursor = self.conn.cursor()
                    cursor.execute(sql)
                    cursor.commit()

                    card_ID = cursor.fetchall()[0][0]
                    request += str(card_ID) + ", "
                request = request[:-2]

                self.cards_ID_to_dropping.append(int(card_ID))
                self.Cards_to_Dropping()

                await websocket.send(request)
            # Розыгрыш карты "Мустанг"
            elif(message_split[0] == "PLAY MUSTANG"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                # Проверка, есть ли у игрока на столе карта "Мустанг"

                sql = "exec dbo.Change_additional_defence_range\n"
                sql += "@player_ID = " + str(player_ID) + ",\n"
                sql += "@n = 1"

                cursor = self.conn.cursor()
                cursor.execute(sql)
                cursor.commit()

                sql = "exec dbo.Change_card_location\n"
                sql += "@card_ID = " + str(card_ID) + ",\n"
                sql += "@card_location = 4"

                cursor = self.conn.cursor()
                cursor.execute(sql)
                cursor.commit()

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Розыгрыш карты "Тюрьма"
            elif(message_split[0] == "PLAY JAIL"):
                player_ID = message_split[1].split(', ')[0]
                target_ID = message_split[1].split(', ')[1]
                card_ID = message_split[2]

                sql = "exec dbo.Passing_card_to_player\n"
                sql = "@player_ID = " + str(target_ID) + ",\n"
                sql = "@card_ID = " + str(card_ID) + ",\n"
                sql = "@card_location = 4"

                cursor = self.conn.cursor()
                cursor.execute(sql)
                cursor.commit()

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))
            # Проверка карты "Тюрьма перед началом хода"
            elif(message_split[0] == "CHECK JAIL"):
                player_ID = message_split[1]
                card_ID = message_split[2]

                sql = "exec dbo.Get_card_for_checking\n"
                sql += "@room_ID = " + str(self.room_ID)

                cursor = self.conn.cursor()
                cursor.execute(sql)
                cursor.commit()

                request = message + "\n"
                check_card_ID = -1
                suit = ""
                for row in cursor:
                    check_card_ID = int(row[0])
                    suit = str(row[2])

                if(suit == "H"):
                    request += "CHECK SUCCESS\n"
                else:
                    request += "CHECK FAIL\n"
                request += str(check_card_ID)
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))


            # Вспомогательные команды
            # Потеря единицы здоровья игроком
            elif(message_split[0] == "LOSE 1 HP"):
                player_ID = message_split[1]

                self.Cards_to_Dropping()

                request = message
                asyncio.get_event_loop().run_until_complete(self.Send_all(request))

            self.conn.close()
        except(Exception):
            print('-1')
            await websocket.send('-1')
            self.conn.close()