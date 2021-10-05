from src.ipc_broker.socket_init import create_publisher
from src.ipc_broker.socket_comms import send_array
from scapy.all import IP, ICMP, sr1
import time

socket = create_publisher(8004)


def pingServer(ip_adrress):
    time.sleep(2)
    isRunning = False
    icmp = IP(dst=ip_adrress) / ICMP()
    resp = sr1(icmp, timeout=10)
    isRunning = resp is not None
    send_array(socket, [isRunning])
    return
