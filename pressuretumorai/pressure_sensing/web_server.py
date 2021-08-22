import socket
import sys
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
    sock.connect(client_address)
    while True:
        data = connection.recv(4)
        print(struct.unpack("<f", data))
        sock.send(b'Message Recieved')


except KeyboardInterrupt:
    connection.close()
    print("Connection closed")
    sys.exit()

