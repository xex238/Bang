import asyncio
import websockets

import os
import pyodbc

import class_room

# recv() - принимаем данные

# print(websocket.remote_address) - данные о клиенте
# print("IP address: ", websocket.remote_address[0]) - IP адрес клиента
# print("port probably: ", websocket.remote_address[1]) - порт клиента

class Server:
    # Данные для подключения к БД
    driver = "Driver={ODBC Driver 17 for SQL Server};"
    server = "Server=den1.mssql8.gear.host;"
    database = "Database=bang;"
    user = "uid=bang;"
    password = "pwd=Ey3V6~-J20D1;"
    TC = "Trusted_Connections=yes;"

    # Подключение к БД
    conn = None

    # Список портов
    registration_port = 8765
    authorization_port = 8766
    get_rooms_port = 8767
    get_achievements_port = 8768
    create_room_port = 8769
    get_room_port_port = 8770

    count_of_rooms = 10 # Количество выделенных портов под игровые комнаты
    rooms = [] # Список с комнатами (с экземплярами класса Room)
    rooms_ports = [] # Список портов для комнат
    rooms_status = [] # Список статусов для портов комнат

    # Конструктор
    def __init__(self):
        for i in range(self.count_of_rooms):
            self.rooms_ports.append(9000 + i)
            self.rooms_status.append(True)

    # Запуск сервера
    def start_server(self):
        registration_server = websockets.serve(self.registration, "localhost", self.registration_port)
        authorization_server = websockets.serve(self.authorization, "localhost", self.authorization_port)
        get_rooms_server = websockets.serve(self.get_rooms, "localhost", self.get_rooms_port)
        get_achievements_server = websockets.serve(self.get_achievements, "localhost", self.get_achievements_port)
        create_room_server = websockets.serve(self.create_room, "localhost", self.create_room_port)
        get_room_port_server = websockets.serve(self.get_room_port, "localhost", self.get_room_port_port)

        asyncio.get_event_loop().run_until_complete(registration_server)
        asyncio.get_event_loop().run_until_complete(authorization_server)
        asyncio.get_event_loop().run_until_complete(get_rooms_server)
        asyncio.get_event_loop().run_until_complete(get_achievements_server)
        asyncio.get_event_loop().run_until_complete(create_room_server)
        asyncio.get_event_loop().run_until_complete(get_room_port_server)

        for i in range(self.count_of_rooms):
            if(not self.rooms_status[i]):
                asyncio.get_event_loop().run_until_complete(self.rooms_server[i])

        asyncio.get_event_loop().run_forever()

    # Соединение с сервером для регистрации пользователей. Коды:
    # 0 - регистрация прошла успешно
    # -1 - возникла ошибка
    # 1 - пользователь с таким логином уже существует в системе
    # 2 - пользователь с данной почтой и паролей уже существует в системе
    async def registration(self, websocket, path):
        # 1) Принимаем регистрационные данные от клиента
        # 2) Отправляем запрос в бд на существование клиента с введённым почтой-паролем и логином
        # 3) Если существует, то отправляем клиенту информацию, что регистрация прошла неуспешно
        # 4) Если не существует, то добавляем данные в бд и говорим, что регистрация прошла успешно
        try:
            self.conn = pyodbc.connect(str(self.driver + self.server + self.database + self.user + self.password + self.TC))

            message = await websocket.recv()
            print("Запрос на регистрацию")
            print(message)

            message_split = message.split('\n')

            mail_ = message_split[0]
            password_ = message_split[1]
            login_ = message_split[2]

            request = "select count(*)\n"
            request += "from [User]\n"
            request += "where [login] = '" + login_ + "'"

            cursor = self.conn.cursor()
            cursor.execute(request)

            result = cursor.fetchall()[0][0]

            if(result == 0):
                request = "select count(*)\n"
                request += "from [User]\n"
                request += "where ([e-mail] = '" + mail_ + "' and [password] = '" + password_ + "')"

                cursor.execute(request)
                result_2 = cursor.fetchall()[0][0]

                if(result_2 == 0):
                    request = "insert into [User]([e-mail], [login], [password])\n"
                    request += "values ('" + mail_ + "', '" + login_ + "', '" + password_ + "')"

                    print(request)

                    cursor.execute(request)
                    self.conn.commit()

                    print('0')
                    await websocket.send('0')
                elif(result_2 == 1):
                    print('2')
                    await websocket.send('2')
                else:
                    print('-1')
                    await websocket.send('-1')
            elif(result == 1):
                print('1')
                await websocket.send('1')
            else:
                print('-1')
                await websocket.send('-1')

            self.conn.close()
        except(Exception):
            await websocket.send('-1')
            self.conn.close()

        print()

    # Соединение с клиентом для авторизации пользователей. Коды:
    # 0 - авторизация прошла успешно
    # -1 - возникла ошибка
    # 1 - пользователь с данной почтой и паролей отсутствует в системе
    async def authorization(self, websocket, path):
        # 1) Принимаем данные от клиента на авторизацию
        # 2) Отправляем запрос в бд на существование записи с полученными данными (логин-пароль)
        # 3) Если существует, то отправляем клиенту информацию, что авторизация прошла успешно
        # 4) Если не существует, то отправляем клиенту информацию, что авторизация прошла не успешно
        try:
            self.conn = pyodbc.connect(str(self.driver + self.server + self.database + self.user + self.password + self.TC))

            message = await websocket.recv()
            print("Запрос на авторизацию")
            print(message)

            message_split = message.split('\n')

            mail_ = message_split[0]
            password_ = message_split[1]

            request = "select count(*)\n"
            request += "from [User]\n"
            request += "where ([e-mail] = '" + mail_ + "' and [password] = '" + password_ + "')"

            cursor = self.conn.cursor()
            cursor.execute(request)

            result = cursor.fetchall()[0][0]

            if(result == 0):
                await websocket.send('1')
            elif(result == 1):
                await websocket.send('0')
            else:
                print('-1')
                await websocket.send('-1')

            self.conn.close()
        except(Exception):
            print('-1')
            await websocket.send('-1')
            self.conn.close()

        print()

    # Получение списка комнат. Коды:
    # 0 - список комнат успешно получен
    # -1 - возникла ошибка
    async def get_rooms(self, websocket, path):
        try:
            self.conn = pyodbc.connect(str(self.driver + self.server + self.database + self.user + self.password + self.TC))

            message = await websocket.recv()

            if(message == "GET ROOMS"):
                print("Запрос на получения списка комнат")

                request = "select ID, count_of_players, max_count_of_players\n"
                request += "from Room\n"
                request += "where ([status] = 'open' and [count_of_players] < [max_count_of_players])"

                cursor = self.conn.cursor()
                cursor.execute(request)

                for row in cursor:
                    print(type(row))
                    print("ID = ", row[0])
                    print("count_of_players = ", row[1])
                    print("max_count_of_players = ", row[2])
                    print()

                await websocket.send('0')

                self.conn.close()
        except(Exception):
            print('-1')
            await websocket.send('-1')
            self.conn.close()

    # Получение списка достижений для определённого пользователя. Коды:
    # 0 - список достижений успешно получен
    # -1 - возникла ошибка
    async def get_achievements(self, websocket, path):
        try:
            self.conn = pyodbc.connect(str(self.driver + self.server + self.database + self.user + self.password + self.TC))

            message = await websocket.recv()

            message_split = message.split('\n')

            mail_ = message_split[0]
            password_ = message_split[1]

            print(websocket.remote_address)
            print("Запрос на получения списка достижений")

            request = "select *\n"
            request += "from Achievements\n"
            request += "join [User]\n"
            request += "on [User].achievements_ID = Achievements.ID\n"
            request += "where ([User].[e-mail] = '" + mail_ + "' and [User].[password] = '" + password_ + "')"

            cursor = self.conn.cursor()
            cursor.execute(request)

            for row in cursor:
                print(row)
                print()

            await websocket.send('0')

            self.conn.close()
        except(Exception):
            print('-1')
            await websocket.send('-1')
            self.conn.close()
    
    # Создание комнаты. Коды:
    # 0 - номер порта и ID комнаты успешно отправлены клиенту
    # -1 - возникла ошибка
    # -2 - свободные комнаты отсутствуют
    async def create_room(self, websocket, path):
        # 1) Принимаем запрос на создание комнаты
        # 2) Создаём запись о новой комнате в БД
        # 3) Получаем ID созданной комнаты (с помощью запроса в БД)
        # 4) Создаём новую комнату на сервере (открываем новый порт для подключения игроков)
        # 5) Отправляем клиенту номер порта для подключения и ID комнаты
        try:
            self.conn = pyodbc.connect(str(self.driver + self.server + self.database + self.user + self.password + self.TC))

            message = await websocket.recv()
            print("Запрос на создание комнаты")
            print(message)

            message_split = message.split('\n')

            mail_ = message_split[0]
            password_ = message_split[1]
            max_count_of_players = message_split[2]

            request = "insert into Room([status], [count_of_players], owner_ID, max_count_of_players)\n"
            request += "values('open', 0, (select ID from [User] where ([e-mail] = '" + mail_ + "' and [password] = '" + password_ + "')), " + max_count_of_players + ")"

            cursor = self.conn.cursor()
            cursor.execute(request)
            self.conn.commit()

            request = "select Room.ID\n"
            request += "from Room\n"
            request += "join [User]\n"
            requset += "on Room.owner_ID = [User].ID\n"
            request += "where ([User].[e-mail] = '" + mail_ + "' and [User].[password] = '" + password_ + "')"

            cursor.execute(request)
            ID = cursor.fetchall()[0][0]

            free_port = -1
            i_port = -1
            for i in range(self.count_of_rooms):
                if(self.rooms_status[i]):
                    free_port = self.rooms_ports[i]
                    i_port = i
                    break

            print("ID = ", ID)
            print("free port = ", free_port)

            if(i_port != -1):
                self.rooms_status[i_port] = False
                self.rooms.append(class_room.Room(max_count_of_players, ID, "localhost", free_port))
                self.rooms[len(self.rooms) - 1].Start_room()

            if(ID == -1):
                await websocket.send('-2')
            else:
                await websocket.send('0')

            self.conn.close()
        except(Exception):
            print('-1')
            await websocket.send('-1')
            self.conn.close()

        print()

    # Получения номера порта при наличии ID игровой комнаты. Коды:
    # 0 - номер порта успешно отправлен клиенту
    # -1 - возникла ошибка
    # -2 - комната с данным номером порта не существует
    async def get_room_port(self, websocket, path):
        try:
            ID = await websocket.recv()
            print("Запрос на получение порта для ID комнаты")
            print(ID)

            room_port = - 1
            for i in range(len(self.rooms)):
                if(self.rooms[i].room_ID == ID):
                    room_port = self.rooms[i].room_port
                    break

            if(room_port == -1):
                await websocket.send('-2')
            else:
                await websocket.send('0')
        except(Exception):
            await websocket.send('-1')