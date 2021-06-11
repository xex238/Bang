import asyncio
import websockets

import os
import pyodbc

import class_room
import class_DB

# recv() - принимаем данные

# print(websocket.remote_address) - данные о клиенте
# print("IP address: ", websocket.remote_address[0]) - IP адрес клиента
# print("port probably: ", websocket.remote_address[1]) - порт клиента

class Server:
    DB = class_DB.DB()

    # Подключение к БД
    conn = None

    # Список портов
    main_port = 8771

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
        main_server = websockets.serve(self.Data_exchange, "localhost", self.main_port)
        asyncio.get_event_loop().run_until_complete(main_server)

        for i in range(self.count_of_rooms):
            if(not self.rooms_status[i]):
                asyncio.get_event_loop().run_until_complete(self.rooms_server[i])

        asyncio.get_event_loop().run_forever()

    # Основной метод класса. Осуществляет приём и обмен сообщениями между клиентом и сервером
    async def Data_exchange(self, websocket, path):
        try:
            self.conn = pyodbc.connect(self.DB.connection_string)

            message = await websocket.recv()
            message_split = message.split('\n')

            print(message)
            print()

            # Регистрация пользователя
            if(message_split[0] == "REGISTRATION"):
                mail = message_split[1]
                password = message_split[2]
                login = message_split[3]

                cursor = self.conn.cursor()
                cursor.execute(self.DB.registration_request.format(mail = mail, password = password, login = login))

                result = str(cursor.fetchall()[0][0])

                if(result == '0'):
                    cursor = self.conn.cursor()
                    cursor.execute(self.DB.registration.format(mail = mail, password = password, login = login))
                    cursor.commit()

                print(result)
                await websocket.send(result)
            # Авторизация пользователя
            elif(message_split[0] == "AUTHORIZATION"):
                mail_ = message_split[1]
                password_ = message_split[2]

                cursor = self.conn.cursor()
                cursor.execute(self.DB.authorization_request.format(mail = mail, password = password))

                result = str(cursor.fetchall()[0][0])

                print(result)
                await websocket.send(result)
            # Получение списка комнат
            elif(message_split[0] == "GET ROOMS"):
                cursor = self.conn.cursor()
                cursor.execute(self.DB.available_rooms)

                answer = "0 OK\n"

                for row in cursor:
                    answer += row[0] + ", " + row[1] + ", " + row[2] + "\n"

                answer = answer[:-1]
                print(answer)
                await websocket.send(answer)
            # Получение списка достижений
            elif(message_split[0] == "GET ACHIEVEMENTS"):
                mail = message_split[1]
                password = message_split[2]

                cursor = self.conn.cursor()
                cursor.execute(self.DB.achivements_request.format(mail = mail, password = password))

                answer = "0 OK\n"
                for row in cursor:
                    answer += str(row[1]) + ", " + str(row[2]) + ", " + str(row[3]) + ", " + str(row[4]) + ", " + str(row[5]) + ", " + str(row[6]) + ", " + str(row[7]) + ", " + str(row[8]) + ", " + str(row[9])

                print(answer)
                await websocket.send(answer)
            # Создание комнаты
            elif(message_split[0] == "CREATE ROOM"):
                mail = message_split[1]
                password = message_split[2]
                max_count_of_players = message_split[3]

                cursor = self.conn.cursor()
                cursor.execute(self.DB.creating_room.format(mail = mail, password = password, max_count_of_players = max_count_of_players))
                cursor.commit()

                ID = str(cursor.fetchall()[0][0])

                free_port = -1
                i_port = -1
                for i in range(self.count_of_rooms):
                    if(self.rooms_status[i]):
                        free_port = self.rooms_ports[i]
                        i_port = i
                        break

                if(i_port != -1):
                    self.rooms_status[i_port] = False
                    self.rooms.append(class_room.Room(max_count_of_players, ID, "localhost", free_port))
                    self.rooms[len(self.rooms) - 1].Start_room()

                answer = "0 OK\n"
                answer += ID + "\n"
                answer += str(free_port)

                print(answer)
                await websocket.send(answer)
            # Получение порта по ID комнаты
            elif(message_split[0] == "GET PORT FOR ROOM ID"):
                ID = message_split[1]

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
        except(Exception) as e:
            await websocket.send('-1')
            print(e)
        finally:
            print("---------------")