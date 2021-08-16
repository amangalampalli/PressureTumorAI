import cv2
from cv2 import aruco
import arucoMarkers
import numpy as np
import pickle

[ret, mtx, dist, rvecs, tvecs] = pickle.load(
    open("calibration/cameraCoeffs.pickle", "rb")
)
cap = cv2.VideoCapture(0)


aruco_dict = markerDict
parameters = aruco.DetectorParameters_create()
parameters.cornerRefinementMethod = (cv2.aruco.CORNER_REFINE_SUBPIX,)
markerWidth = 0.0508

board_ids = np.array([[0], [1], [2], [3], [4], [5]], dtype=np.int32)
board_corners = [
    np.array(
        [
            [-0.022, 0.023, 0.03],
            [0.023, 0.022, 0.03],
            [0.023, -0.023, 0.03],
            [-0.022, -0.023, 0.03],
        ],
        dtype=np.float32,
    ),
    np.array(
        [
            [-0.022, -0.03, 0.022],
            [0.023, -0.03, 0.022],
            [0.022, -0.03, -0.022],
            [-0.022, -0.03, -0.022],
        ],
        dtype=np.float32,
    ),
    np.array(
        [
            [-0.03, -0.023, 0.022],
            [-0.03, -0.022, -0.023],
            [-0.03, 0.023, -0.022],
            [-0.03, 0.023, 0.023],
        ],
        dtype=np.float32,
    ),
    np.array(
        [
            [-0.022, -0.022, -0.03],
            [0.023, -0.023, -0.03],
            [0.023, 0.023, -0.03],
            [-0.022, 0.023, -0.03],
        ],
        dtype=np.float32,
    ),
    np.array(
        [
            [0.03, -0.023, -0.022],
            [0.03, -0.023, 0.023],
            [0.03, 0.023, 0.022],
            [0.03, 0.022, -0.023],
        ],
        dtype=np.float32,
    ),
    np.array(
        [
            [-0.022, 0.03, -0.023],
            [0.023, 0.03, -0.022],
            [0.023, 0.03, 0.023],
            [-0.022, 0.03, 0.022],
        ],
        dtype=np.float32,
    ),
]
board = aruco.Board_create(board_corners, aruco_dict, board_ids)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, rejectedImgPoints = aruco.detectMarkers(
        gray, aruco_dict, parameters=parameters
    )

    if np.all(ids != None):
        rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners, 0.05, mtx, dist)
        for i in range(len(ids)):
            frame = aruco.drawAxis(frame, mtx, dist, rvec[i], tvec[i], 0.1)
            frame = aruco.drawDetectedMarkers(frame, corners, ids)

    # Display the resulting frame
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
