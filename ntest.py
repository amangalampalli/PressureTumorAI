import cv2

from src.ipc_broker.socket_comms import recv_array
from src.ipc_broker.socket_init import create_subscriber

socket = create_subscriber(8002)

while True:
    img = recv_array(socket)[0]
    cv2.imshow("test", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
