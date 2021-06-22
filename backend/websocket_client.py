import asyncio
import websockets

class_server_port = 8771
room_port = 8780
room_ID = 22

test_port = 8801

async def hello():
    uri = "ws://localhost:" + str(class_server_port)
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

async def registration():
    # 1) Отправка авторизационных данных на сервер
    # 2) Получение ответа от сервера
    # 3) Обработка полученного ответа
    uri = "ws://localhost:" + str(class_server_port)
    async with websockets.connect(uri) as websocket:
        #message = "mail=dima040998@yandex.ru\n"
        #message += "password=12345\n"
        #message += "login=xex238"

        #message = "dima040998@yandex.ru\n"
        #message += "12345\n"
        #message += "xex238"

        #message = "ivan@yandex.ru\n"
        #message += "12345\n"
        #message += "xex238"

        #message = "dima040998@yandex.ru\n"
        #message += "12345\n"
        #message += "ivan238"

        message = "REGISTRATION\n"
        message += "alyona@yandex.ru\n"
        message += "12345\n"
        message += "alyona238"

        print(message)
        print()
        await websocket.send(message)

        result = await websocket.recv()
        print(result)
        print("---------------")
  
async def authorization():
    # 1) Отправка регистрационных данных на сервер
    # 2) Получение ответа от сервера
    # 3) Обработка полученного ответа
    uri = "ws://localhost:" + str(class_server_port)
    async with websockets.connect(uri) as websocket:
        #message = "mail=dima040998@yandex.ru\n"
        #message += "password=12345\n"
        #message += "login=xex238"

        #message = "dima040998@yandex.ru\n"
        #message += "12345\n"
        #message += "xex238"

        #message = "ivan@yandex.ru\n"
        #message += "12345\n"
        #message += "xex238"

        #message = "dima040998@yandex.ru\n"
        #message += "12345\n"
        #message += "ivan238"

        message = "AUTHORIZATION\n"
        message += "alyona@yandex.ru\n"
        message += "12345"

        print(message)
        print()
        await websocket.send(message)

        result = await websocket.recv()
        print(result)
        print("---------------")
    
async def get_rooms():
    # 1) Отправка запроса на сервер на получение списка комнат
    # 2) Получение ответа от сервера
    # 3) Обработка полученного ответа
    uri = "ws://localhost:" + str(class_server_port)
    async with websockets.connect(uri) as websocket:
        request = "GET ROOMS"
        print(request)
        print()

        await websocket.send(request)

        result = await websocket.recv()
        print(result)
        print("---------------")
  
async def get_achievements():
    # 1) Отправка запроса на сервер на получение списка комнат
    # 2) Получение ответа от сервера
    # 3) Обработка полученного ответа
    uri = "ws://localhost:" + str(class_server_port)
    async with websockets.connect(uri) as websocket:
        message = "GET ACHIEVEMENTS\n"
        message += "dima040998@yandex.ru\n"
        message += "12345"

        message = "GET ACHIEVEMENTS\n"
        message += "alyona@yandex.ru\n"
        message += "12345"

        print(message)
        print()

        await websocket.send(message)

        result = await websocket.recv()
        print(result)
        print("---------------")

async def create_room():
    # 1) Отправка запроса на сервер на получение списка комнат
    # 2) Получение ответа от сервера
    # 3) Обработка полученного ответа
    uri = "ws://localhost:" + str(class_server_port)
    async with websockets.connect(uri) as websocket:
        message = "CREATE ROOM\n"
        message += "alyona@yandex.ru\n"
        message += "12345\n"
        message += "6"

        print(message)
        print()

        await websocket.send(message)

        result = await websocket.recv()
        print(result)
        print("---------------")

async def get_port_for_room_ID():
    uri = "ws://localhost:" + str(class_server_port)
    async with websockets.connect(uri) as websocket:
        message = "GET PORT FOR ROOM ID\n"
        message += str(room_ID)

        print(message)
        print()

        await websocket.send(message)

        result = await websocket.recv()
        room_port = int(result.split('\n')[1])
        print(result)
        print("---------------")

async def room_message():
    uri = "ws://localhost:8780"
    async with websockets.connect(uri) as websocket:
        message = "HELLO\n"
        message += "alyona@yandex.ru\n"
        message += "12345\n"
        message += "localhost\n"
        message += str(test_port)

        #message = "SET READY\n"
        #message += "TRUE\n"
        #message += "40"

        #message = "START PLANNING STAGE\n"
        #message += "38"

        print(message)
        print()

        await websocket.send(message)

        result = await websocket.recv()
        print(result)
        print("---------------")

# Постоянно запущенный процесс, принимающий сообщения
async def test_get_message(self, websocket, path):
    result = await websocket.recv()
    print(result)
    print("---------------")

async def send_message():
    uri = "ws://localhost:8800"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Проверка связи")

async def start_client():
    test_server = websockets.serve(test_get_message, "localhost", test_port)
    asyncio.get_event_loop().run_until_complete(test_server)
    asyncio.get_event_loop().run_forever()

start_client()

#asyncio.get_event_loop().run_until_complete(registration())
#asyncio.get_event_loop().run_until_complete(authorization())
#asyncio.get_event_loop().run_until_complete(get_rooms())
#asyncio.get_event_loop().run_until_complete(get_achievements())
#asyncio.get_event_loop().run_until_complete(create_room())
#asyncio.get_event_loop().run_until_complete(get_port_for_room_ID())
asyncio.get_event_loop().run_until_complete(room_message())