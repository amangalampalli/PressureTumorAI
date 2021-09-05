import socket
import sys
import struct

def startServer():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = socket.gethostname()
    port = 8000
    server_address = (host, port)
    print("Server starting up at " + str(server_address))
    sock.bind(server_address)

    sock.listen(1)

    print("Waiting for connection")
    connection, client_address = sock.accept()

    try:
        print("Connection from " + str(client_address))
        while True:
            data = connection.recv(4)
            print(struct.unpack("<f", data)[0])
            connection.sendall(data)
    except:
        connection.close()
        print("Connection closed")
    sys.exit()

