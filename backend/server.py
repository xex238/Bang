import class_server
import class_room

#my_server = class_server.Server()
#my_server.start_server()

room = class_room.Room(4, 10, "localhost", 8780)
room.Start_server()