import cv2
import numpy as np
from src.ipc_broker.socket_init import create_subscriber
from src.ipc_broker.socket_comms import recv_array, recv_another_array


def showFrames():
    socket = create_subscriber(8001)
    while True:
        data = recv_another_array(socket)
        print(data[0])
        cv2.imshow("frame", data[0])
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    showFrames()
