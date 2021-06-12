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
    # Экземпляр класса со списком команд для базы данных
    DB = class_DB.DB() 

    # Подключение к БД
    conn = None

    # Список портов
    main_port = 8771 # Порт для обмена сообщениями Клиент - Сервер

    start_room_port = 8780 # Начальный порт для комнат
    count_of_rooms = 10 # Количество выделенных портов под игровые комнаты
    rooms = []
    rooms_servers = [] # Списов серверов для комнат (экземпляров класса "Room_server")
    rooms_ports = []
    rooms_status = []

    # Конструктор
    def __init__(self):
        #for i in range(self.count_of_rooms):
        #    self.rooms_status[self.start_room_port + i] = False

        for i in range(self.count_of_rooms):
            #self.rooms.append(class_room.Room(max_count_of_players, ID, "localhost", self.start_room_port + i))
            self.rooms_ports.append(self.start_room_port + i)
            self.rooms_status.append(True)
            #self.rooms_servers.append(websockets.serve(self.rooms[i].Data_exchange, "localhost", self.main_port))

    # Запуск сервера
    def start_server(self):
        main_server = websockets.serve(self.Data_exchange, "localhost", self.main_port)
        asyncio.get_event_loop().run_until_complete(main_server)

        for i in range(self.count_of_rooms):
            if(not self.rooms_status[i]):
                asyncio.get_event_loop().run_until_complete(self.rooms_servers[i])

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

                for row in cursor:
                    result = str(row[0])

                if(result == '0'):
                    cursor = self.conn.cursor()
                    cursor.execute(self.DB.registration.format(mail = mail, password = password, login = login))
                    cursor.commit()

                print(result)
                await websocket.send(result)
            # Авторизация пользователя
            elif(message_split[0] == "AUTHORIZATION"):
                mail = message_split[1]
                password = message_split[2]

                cursor = self.conn.cursor()
                cursor.execute(self.DB.authorization_request.format(mail = mail, password = password))

                for row in cursor:
                    result = str(row[0])

                print(result)
                await websocket.send(result)
            # Получение списка комнат
            elif(message_split[0] == "GET ROOMS"):
                cursor = self.conn.cursor()
                cursor.execute(self.DB.available_rooms)

                answer = "0 OK\n"

                for row in cursor:
                    answer += str(row[0]) + ", " + str(row[1]) + ", " + str(row[2]) + "\n"

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

                print(self.DB.creating_room.format(mail = mail, password = password, max_count_of_players = max_count_of_players))

                cursor = self.conn.cursor()
                cursor.execute(self.DB.creating_room.format(mail = mail, password = password, max_count_of_players = max_count_of_players))
                #cursor.commit()

                for row in cursor:
                    print(str(row[0]))
                    room_ID = str(row[0])
                print()

                free_port = -1
                i_port = -1
                for i in range(self.count_of_rooms):
                    if(self.rooms_status[i]):
                        free_port = self.rooms_ports[i]
                        i_port = i
                        break

                print("free_port = ", free_port)
                print("i_port = ", i_port)

                if(i_port != -1):
                    self.rooms_status[i_port] = False

                    self.rooms.append(class_room.Room(max_count_of_players, room_ID, "localhost", free_port))
                    self.rooms_servers.append(websockets.serve(self.rooms[len(self.rooms) - 1].Data_exchange, "localhost", free_port))

                answer = "0 OK\n"
                answer += room_ID + "\n"
                answer += str(free_port)

                print(answer)
                await websocket.send(answer)
            # Закрытие комнаты
            elif(message_split[0] == "CLOSE ROOM"):
                room_ID = message_split[0]

                for i in range(len(self.rooms)):
                    if(str(room_ID) == str(self.rooms[i].room_ID)):
                        room_port = self.rooms[i].room_port
                        for j in range(len(self.rooms_ports)):
                            if(room_port == self.rooms_ports[j]):
                                self.rooms_status[j] = True
                        self.rooms_servers.pop(i)
                        self.rooms.pop(i)
                        break
            # Получение порта по ID комнаты
            elif(message_split[0] == "GET PORT FOR ROOM ID"):
                room_ID = message_split[1]

                room_port = - 1
                for i in range(len(self.rooms)):
                    if(str(self.rooms[i].room_ID) == str(room_ID)):
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