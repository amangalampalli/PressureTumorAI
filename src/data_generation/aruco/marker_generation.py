import cv2
import numpy as np

pathToMarkers = (
    "/Users/aditya/Programming/PressureTumorAI/data/marker_dataset/pngImages/"
)
markerDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)


def generateMarkers(numMarkers, size):
    for x in range(numMarkers):
        markerImage = np.zeros((size, size), dtype=np.uint8)
        markerImage = cv2.aruco.drawMarker(markerDict, x, size, markerImage, 1)
        markerPath = pathToMarkers + str((x + 1)) + ".png"
        print(markerPath)
        cv2.imwrite(markerPath, markerImage)


if __name__ == "__main__":
    generateMarkers(12, 400)
