import cv2
import numpy as np
from src.localization.aruco_tracking import localization
from src.ipc_broker.socket_init import create_publisher
from src.ipc_broker.socket_comms import send_array, send_another_array


def stream_frames():
    socket = create_publisher(8002)
    cap = cv2.VideoCapture(0)
    positionList = [None, None]
    while True:
        ret, frame = cap.read()
        if ret:
            position = localization(frame, positionList)
            send_another_array(socket, position)
        else:
            continue


if __name__ == "__main__":
    stream_frames()
