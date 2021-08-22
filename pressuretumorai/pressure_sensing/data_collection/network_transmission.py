# type: ignore
import struct
import socket
import sys
import random
import struct
# from machine import Pin
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('10.0.0.73', 8000)
print("Connecting to server " + str(server_address))
sock.connect(server_address)
# led = Pin(2, Pin.OUT)


try:
    print("Connected")
    while True:
        # led.low()
        message = random.uniform(0, 100)
        print("Sending message: " + str(message))
        sock.send(struct.pack('<f', message))
        # led.high()


finally:
    print("Closing connection")
    sock.close()