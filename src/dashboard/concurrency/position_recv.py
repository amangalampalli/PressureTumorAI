from src.ipc_broker.socket_init import create_subscriber
from src.ipc_broker.socket_comms import recv_array
import random

socket = create_subscriber(8002)


def return_position():
    """
    Return the position of the stylus
    """
    return random.random()
    # return recv_array(socket)[1]
