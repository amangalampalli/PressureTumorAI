import zmq
import msgpack
import msgpack_numpy as m
import numpy as np


def send_message(socket, message):
    """
    Send a message to the IPC broker through a pub/sub system.

    Args:
        message (str): The message to send.

    Returns:
        None
    """
    return socket.send(message)


def recv_message(socket):
    """
    Receive a message from the IPC broker through a pub/sub system.

    Args:
        None

    Returns:
        Object: The message received.
    """
    return socket.recv()


def send_array(socket, A, flags=0, copy=True, track=False):
    return socket.send(
        msgpack.packb(A, default=m.encode), flags, copy=copy, track=track
    )


def recv_array(socket, flags=zmq.NOBLOCK, copy=True, track=False):
    """recv a numpy array"""
    msg = socket.recv(flags=flags, copy=copy, track=track)
    return msgpack.unpackb(msg, object_hook=m.decode)
