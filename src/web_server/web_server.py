import socket
import struct
import numpy as np
from scapy.all import *

from src.ipc_broker.socket_init import create_publisher
from src.ipc_broker.socket_comms import send_array

pubSocket = create_publisher(8001)


def runServer():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = socket.gethostname()
    port = 8000
    server_address = (host, port)
    print("Server starting up at " + str(server_address))
    sock.bind(server_address)
    print("Waiting for connection")
    connection, client_address = sock.accept()
    print("Connection from " + str(client_address))
    while True:
        try:
            data = connection.recv(4)
            message = struct.unpack("<f", data)[0]
            connection.sendall(data)
            send_array(pubSocket, np.array([message, pingServer(client_address)]))
        except:
            connection.close()
            print("Connection closed")


def pingServer(ip_adrress):
    isRunning = False
    icmp = IP(dst=ip_adrress) / ICMP()
    resp = sr1(icmp, timeout=10)
    isRunning = resp is not None
    return isRunning
