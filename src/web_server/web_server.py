import socket
import struct

# from src.data_processing.filewriter import writeFile
# from src.localization.stylus import getCubePosition

# def startServer():
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     host = socket.gethostname()
#     port = 8000
#     server_address = (host, port)
#     print("Server starting up at " + str(server_address))
#     sock.bind(server_address)

#     sock.listen(1)

#     print("Waiting for connection")
#     connection, client_address = sock.accept()

#     try:
#         print("Connection from " + str(client_address))
#         while True:
#             data = connection.recv(4)
#             message = (struct.unpack("<f", data)[0])
#             position = getCubePosition()
#             writeFile(str(position) + ", " + str(message))
#             print("Received: " + str(message) + " and tip's position is " + str(position))
#             connection.sendall(data)
#     except:
#         connection.close()
#         print("Connection closed")


def initSocket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = socket.gethostname()
    port = 8000
    server_address = (host, port)
    print("Server starting up at " + str(server_address))
    sock.bind(server_address)
    notConnected = True
    print("Waiting for connection")
    while notConnected:
        try:
            connection, client_address = sock.accept()
            notConnected = False
        except:
            pass
    print("Connection from " + str(client_address))
    return connection, client_address


def runServer(connection, client_address):
    try:
        data = connection.recv(4)
        message = struct.unpack("<f", data)[0]
        connection.sendall(data)
    except:
        connection.close()
        print("Connection closed")
    if message is not None:
        return message
    else:
        return 0
