import cv2
import time
from multiprocessing import Process

TOTAL_PICTURES = 100
CURRENT_PICTURES = 0


def readFrame():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow(
            "frame",
            cv2.resize(frame, (int(frame.shape[1] / 2), int(frame.shape[0] / 2))),
        )
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()


def writeFrame():
    global TOTAL_PICTURES, CURRENT_PICTURES
    cap = cv2.VideoCapture(0)
    while CURRENT_PICTURES < TOTAL_PICTURES:
        ret, frame = cap.read()
        time.sleep(0.7)
        cv2.imwrite(
            "/Users/aditya/Programming/Pressure-Based-Tumor-Detection/callibration/dataset/"
            + str(CURRENT_PICTURES)
            + ".png",
            frame,
        )
        print(str(CURRENT_PICTURES) + " Picture taken")
        CURRENT_PICTURES += 1


if __name__ == "__main__":
    p1 = Process(target=readFrame)
    p1.start()
    p2 = Process(target=writeFrame)
    p2.start()
    p1.join()
    p2.join()
