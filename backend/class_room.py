import asyncio
import websockets
import random

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
    players_characters_list_ID = [] # Список из 3-ёх ID персонажей для каждого игрока
    players_characters_ID = [] # Список ID персонажей участников комнаты

    players_queue = [] # 
    player_ID_step = -1 # ID игрока, который ходит в данный момент

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
            await websocket.send(request)

    # Отправка сообщения всем игрокам
    async def Send_all(self, message):
        for i in range(len(self.players_ID)):
            uri = "ws://" + self.room_IP[i] + ":" + self.room_port[i]
            async with websockets.connect(uri) as websocket:
                await websocket.send(request)

    # Отправка сообщения всем игрокам, кроме одного
    async def Send_all_except_one(self, message, player_ID):
        for i in range(len(self.players_ID)):
            if(self.players_ID[i] != player_ID):
                uri = "ws://" + self.room_IP[i] + ":" + self.room_port[i]
                async with websockets.connect(uri) as websocket:
                    await websocket.send(request)

    # Основной метод класса. Осуществляет приём и обмен сообщениями между участниками комнаты
    async def Data_exchange(self, websocket, path):
        try:
            self.conn = pyodbc.connect(str(self.driver + self.server + self.database + self.user + self.password + self.TC))

            message = await websocket.recv()
            message_split = message.split('\n')

            # Присоединение пользователя к комнате
            if((len(message_split[0]) == 5) and (message_split[0] == "HELLO")):
                # Если комната не полная, то принимаем подключение
                if((self.count_of_players >= 0) and (self.count_of_players < self.max_count_of_players)):
                    mail = message_split[1]
                    password = message_split[2]

                    # Запрос на добавление пользователя в комнату
                    # Получение из БД:
                    # Из таблицы Rooms: count_of_players, max_count_of_players
                    # Из таблицы User: user_ID

                    request = "HELLO\n"
                    request += count_of_players + ", " + max_count_of_players + "\n"
                    request += user_ID

                    self.players_ID.append(user_ID)
                    self.players_status.append(False)
                    self.players_IP.append(websocket.remote_address[0])
                    self.players_port.append(websocket.remote_address[1])

                    self.players_characters_ID.append(-1)
                    self.players_roles_ID.append(-1)

                    self.count_of_players = self.count_of_players + 1
                    await websocket.send(request)

                    request = "NEW PLAYER\n"
                    request += count_of_players

                    asyncio.get_event_loop().run_until_complete(self.Send_all_except_one(request, user_ID))
                # Если комната полная, то отклоняем подключение
                elif(self.count_of_players == self.max_count_of_players):
                    await websocket.send("FORBIDDEN 1")
                else:
                    await websocket.send("FORBIDDEN 2")
            # Изменение статуса готовности игрока (без запроса в БД)
            elif((len(message_split[0]) == 9) and (message_split[0] == "SET READY")):
                player_ID = message_split[2]
                if(message_split[1] == "TRUE"):
                    self.players_status[self.Get_i(player_ID)] = True
                elif(message_split[1] == "FALSE"):
                    self.players_status[self.Get_i(player_ID)] = False
                await websocket.send("0 OK")
                asyncio.get_event_loop().run_until_complete(self.Send_all_except_one(message, player_ID))
            # Начало стадии планирования
            elif((len(message_split[0]) == 20) and (message_split[0] == "START PLANNING STAGE")):
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
                    

                # Запрос на получение 3 * count_of_players случайных персонажей
                # Запрос на получение max_count_of_players случайных ролей (по правилам выдачи ролей)
                # Генерация порядкового номера для каждого игрока
                for i in range(self.count_of_players):
                    self.players_queue[i] = i + 1
                random.shuffle(self.players_queue)
            # Запрос на получение 3-ёх случайных персонажей (без запроса в БД)
            elif((len(message_split[0]) == 16) and (message_split[0] == "GET 3 CHARACTERS")):
                player_ID = message_split[1]

                request = "GET 3 CHARACTERS\n"
                request += self.players_characters_list_ID[self.Get_i(player_ID)][0] + "\n"
                request += self.players_characters_list_ID[self.Get_i(player_ID)][1] + "\n"
                request += self.players_characters_list_ID[self.Get_i(player_ID)][2]

                await websocket.send(request)
            # Выбор одного из 3-ёх случайных персонажей
            elif((len(message_split[0]) == 13) and (message_split[0] == "SET CHARACTER")):
                character_ID = message_split[1].split(', ')[0]
                player_ID = message_split[2]

                self.players_characters_ID[self.Get_i(player_ID)] = character_ID

                # Отправление запроса на создание записи в таблице "Character"
                await websocket.send("0 OK")
            # Запрос на получение роли
            elif((len(message_split[0]) == 8) and (message_split[0] == "GET ROLE")):
                player_ID = message_split[1]

                # Отправка запроса в бд на создание записи в таблице "Role"

                request = "SET ROLE\n"
                request += self.players_roles_ID[self.Get_i(player_ID)]
                await websocket.send(request)
            # Приём подтверждение готовности игрока к передаче данных о других игроках (без запроса в БД)
            elif((len(message_split[0]) == 27) and (message_split[0] == "CHARACTER AND ROLE SELECTED")):
                # Изменение статуса игрока
                player_ID = message_split[1]
                self.players_status[self.Get_i(player_ID)] = True

                await websocket.send("0 OK")
            # Приём запроса на отправку данных о других игроках (без запроса в БД)
            elif((len(message_split[0]) == 16) and (message_split[0] == "GET PLAYERS INFO")):
                player_ID = message_split[1]
                request = self.players_queue[self.Get_i(player_ID)] + "\n"
                for i in range(len(self.players_ID) - 1):
                    request += str(i + 1) + ", " + self.players_ID[i] + ", " + self.players_characters_ID[i] + "\n"
                request += str(len(self.players_ID) - 1 + 1) + ", " + self.players_ID[len(self.players_ID) - 1] + ", " + self.players_characters_ID[len(self.players_ID) - 1]

                await websocket.send(reequest)
            # Приём запроса на получение стартовых карт
            elif((len(message_split[0]) == 15) and (message_split[0] == "GET START CARDS")):
                # Генерация стартовых карт для игрока
                request = "SET START CARDS\n"
                for i in range(count_of_cards - 1):
                    request += cards_ID[i] + ", " + cards_name[i] + "\n"
                request += cards_ID[count_of_cards - 1] + ", " + cards_name[count_of_cards - 1]

                await websocket.send(request)
            # Приём подтверждения готовности к началу игры (без запроса в БД)
            elif((len(message_split[0]) == 10) and (message_split[0] == "START GAME")):
                player_ID = message_split[1]
                self.players_status[self.Get_i(player_ID)] = True

                all_is_ready = True
                for i in range(len(self.players_status)):
                    if(not self.players_status[i]):
                        all_is_ready = False
                        break

                if(all_is_ready):
                    asyncio.get_event_loop().run_until_complete(self.Send_all("GAME IS START"))
            self.conn.close()
        except(Exception):
            print('-1')
            await websocket.send('-1')
            self.conn.close()