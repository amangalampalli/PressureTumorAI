# type: ignore

import machine
from machine import Pin
import socket
import sys
import random
import struct
import time
from time import sleep

button = Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
led = Pin(2, Pin.OUT)
led.off()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("10.0.0.73", 8000)
print("Connecting to server " + str(server_address))
sock.connect(server_address)

try:
    print("Connected")
    while True:
        led.off()
        message = float(random.getrandbits(32) / 100)
        print("Sending message: " + str(message))
        sock.send(struct.pack("<f", message))
        data = sock.recv(4)
        if data != message:
            Exception("Message not correct")
        led.on()

except:
    print("Closing connection")
    sock.close()
    sys.exit(0)
