import asyncio
import websockets

import os
import pyodbc

#import class_room

# recv() - принимаем данные

# print(websocket.remote_address) - данные о клиенте
# print("IP address: ", websocket.remote_address[0]) - IP адрес клиента
# print("port probably: ", websocket.remote_address[1]) - порт клиента

class Server:
    # Данные для подключения к БД
    driver = "Driver={ODBC Driver 17 for SQL Server};"
    server = "Server=den1.mssql8.gear.host;"
    database = "Database=bang2;"
    user = "uid=bang2;"
    password = "pwd=Tv08Yk-D8nZ?;"
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

            #request = "select dbo.Registration_request(''?'', ''?'', ''?'')"
            #values = (mail_, password_, login_)
            request = "select dbo.Registration_request('" + mail_ + "', '" + password_ + "', '" + login_ + "')"
            print("request = ", request)

            cursor = self.conn.cursor()
            cursor.execute(request)

            result = cursor.fetchall()[0][0]
            result_ = str(result)
            print("result = ", result_)

            if(result_ == '0'):
                print("Добавление данных в таблицу [User]")

                request = "exec dbo.Registration\n"
                request += "@mail = '" + mail_ + "',\n"
                request += "@password = '" + password_ + "',\n"
                request += "@login = '" + login_ + "'"
                print(request)

                cursor = self.conn.cursor()
                cursor.execute(request)
                cursor.commit()

            await websocket.send(result_)

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

            request = "select dbo.Authorization_request('" + mail_ + "', '" + password_ + "')"

            cursor = self.conn.cursor()
            cursor.execute(request)

            result = cursor.fetchall()[0][0]
            result_ = str(result)
            print("result_ = ", result_)

            await websocket.send(result_)

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

                request = "exec dbo.Available_rooms"

                cursor = self.conn.cursor()
                cursor.execute(request)

                answer = "0 OK\n"

                for row in cursor:
                    print(type(row))
                    print("ID = ", row[0])
                    print("count_of_players = ", row[1])
                    print("max_count_of_players = ", row[2])
                    answer += row[0] + ", " + row[1] + ", " + row[2] + "\n"
                    print()

                answer = answer[:-1]
                print("answer = ", answer)
                await websocket.send(answer)

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

            request = "exec dbo.Achivements_request\n"
            request += "@mail = '" + mail_ + "',\n"
            request += "@password = '" + password_ + "'"
            print(request)

            cursor = self.conn.cursor()
            cursor.execute(request)

            answer = "0 OK\n"

            for row in cursor:
                answer += str(row[1]) + ", " + str(row[2]) + ", " + str(row[3]) + ", " + str(row[4]) + ", " + str(row[5]) + ", " + str(row[6]) + ", " + str(row[7]) + ", " + str(row[8]) + ", " + str(row[9])
                print(row)
                print()

            print(answer)
            await websocket.send(answer)

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

            request = "exec dbo.Creating_room\n"
            request += "@mail = '" + mail_ + "',\n"
            request += "@password = '" + password_ + "',\n"
            request += "@max_count_of_players = " + max_count_of_players

            cursor = self.conn.cursor()
            cursor.execute(request)
            #cursor.commit()

            ID = cursor.fetchall()[0][0]
            ID_ = str(ID)

            free_port = -1
            i_port = -1
            for i in range(self.count_of_rooms):
                if(self.rooms_status[i]):
                    free_port = self.rooms_ports[i]
                    i_port = i
                    break

            print("room_ID = ", ID_)
            print("free port = ", free_port)

            #if(i_port != -1):
            #    self.rooms_status[i_port] = False
            #    self.rooms.append(class_room.Room(max_count_of_players, ID, "localhost", free_port))
            #    self.rooms[len(self.rooms) - 1].Start_room()

            answer = "0 OK\n"
            answer += ID_ + "\n"
            answer += str(free_port)

            await websocket.send(answer)

            self.conn.close()
        except(Exception) as e:
            print("Exception:\n")
            print(e)
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

            answer = "0 OK\n"
            answer += str(room_port)

            if(room_port == -1):
                await websocket.send('-2')
            else:
                await websocket.send(answer)
        except(Exception):
            await websocket.send('-1')