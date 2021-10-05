from PIL import Image, ImageTk
from tkinter import Label
import cv2
from src.ipc_broker.socket_init import create_subscriber
from src.ipc_broker.socket_comms import recv_array

socket = create_subscriber(8002, isImage=True)

backupImg = None


def return_frame():
    global backupImg
    # Get the latest frame and convert into Image
    raw_image = None
    try:
        raw_image = recv_array(socket)[0]
    except:
        return backupImg
    cv2image = cv2.resize(cv2.cvtColor(raw_image, cv2.COLOR_BGR2RGB), (610, 343))
    img = Image.fromarray(cv2image)
    backupImg = ImageTk.PhotoImage(image=img)
    return backupImg
