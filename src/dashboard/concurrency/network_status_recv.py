from src.ipc_broker.socket_init import create_subscriber
from src.ipc_broker.socket_comms import recv_array
import random

socket = create_subscriber(8004)

backupStatus = None


def return_network_status():
    global backupStatus
    # if recv_array(socket) is not None:
    #     backupStatus = recv_array(socket)
    #     return backupStatus
    # else:
    #     return backupStatus
    return random.choice([True, False])
