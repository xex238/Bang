import asyncio
import websockets

class Room:
    room_ID = -1 # ID комнаты (аналогичен значению в БД)
    room_status = "open" # Статус комнаты (аналогичен значению в БД)
    room_IP = None # IP адрес комнаты
    room_port = None # Порт комнаты

    server = None # Сервер комнаты

    players_ID = [] # Список ID участников комнаты
    players_IP = [] # Список IP адресов участников комнаты
    players_port = [] # Список портов участников комнаты

    player_ID_step = -1 # ID игрока, который ходит в данный момент

    def __init__(self, room_ID, room_IP, room_port):
        self.room_ID = room_ID
        self.room_IP = room_IP
        self.room_port = room_port

    # Открытие (запуск) комнаты
    def Start_room(self):
        self.server = websockets.serve(self.Data_exchange, self.room_IP, self.room_port)
        asyncio.get_event_loop().run_until_complete(self.server)
        asyncio.get_event_loop().run_forever()

    async def Send_all(self, message):
        for i in range(len(self.players_ID)):
            uri = "ws://" + self.room_IP[i] + ":" + self.room_port[i]
            async with websockets.connect(uri) as websocket:
                await websocket.send(request)

    async def Data_exchange(self, websocket, path)
        try:
            self.conn = pyodbc.connect(str(self.driver + self.server + self.database + self.user + self.password + self.TC))

            message = await websocket.recv()

            message_split = message.split('\n')

            # Присоединение пользователя к комнате
            if(message_split[0] == 'HELLO'):
                mail = message_split[1]
                password = message_split[2]

                # Запрос на добавление пользователя в комнату
                # Получение из БД:
                # Из таблицы Rooms: count_of_players, max_count_of_players
                # Из таблицы User: user_ID

                request = "HELLO\n"
                request += count_of_players + ", " + max_count_of_players + "\n"
                request += user_ID

                await websocket.send(request)
            # Изменение статуса готовности игрока
            elif((len(message_split[0]) > 7) and (message_split[0][0:5] == "READY")):
                # Изменение значения поля "is_ready" в таблице "Player"
                if(message_split[0][7:12] == "TRUE"):
                    # Запрос в БД на изменение значения поля "is_ready" в таблице "Player"
                elif(message_split[0][7:13] == "FALSE"):
                    # Запрос в БД на изменение значения поля "is_ready" в таблице "Player"
                    asyncio.get_event_loop().run_until_complete(self.Send_all(message))
            # Приём выбранного персонажа
            elif((len(message_split[0]) > 10) and (message_split[0][0:8] == "SET ROLE")):
                player_name = message_split[0][10::]
                player_ID = message_split[1]
                character_ID = message_split[2]
                # Отправление запроса на создание записи в таблице "Character"

                await websocket.send("OK")
            # Приём запроса на начало игры
            elif((len(message_split[0]) == 10) and (message_split[0] == "START GAME")):
                asyncio.get_event_loop().run_until_complete(self.Send_all("GAME IS STARTING"))

            self.conn.close()
        except(Exception):
            print('-1')
            await websocket.send('-1')
            self.conn.close()