import zmq


def create_publisher(port):
    """
    Create a publisher socket.

    Args:
        port (int): The port to start server at.

    Returns:
        zmq.Socket: The publisher socket.
    """
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:%s" % port)
    return socket


def create_subscriber(port):
    """
    Create a subscriber socket.

    Args:
        port (int): The port to connect to.

    Returns:
        zmq.Socket: The subscriber socket.
    """
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:%s" % port)
    socket.setsockopt_string(zmq.SUBSCRIBE, "")
    return socket
