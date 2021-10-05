import random
from src.ipc_broker.socket_init import create_subscriber
from src.ipc_broker.socket_comms import recv_array

socket = create_subscriber(8001)


def return_pressure():
    """
    Returns the pressure value from the pressure sensor.
    """
    return random.random()
    # return recv_array(socket)[0]
