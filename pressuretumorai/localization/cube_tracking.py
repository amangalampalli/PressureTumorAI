import cv2
from cv2 import aruco
from pressuretumorai.aruco_markers.markerGen import markerDict
import numpy as np
import pickle

[ret, mtx, dist, rvecs, tvecs] = pickle.load(
    open("pressuretumorai/calibration/cameraCoeffs.pickle", "rb")
)
cap = cv2.VideoCapture(0)


aruco_dict = markerDict
parameters = aruco.DetectorParameters_create()
parameters.cornerRefinementMethod = aruco.CORNER_REFINE_SUBPIX
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

rvec = None
tvec = None
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, rejectedImgPoints = aruco.detectMarkers(
        gray, aruco_dict, parameters=parameters
    )
    corners, ids, rejectedImgPoints, recoveredIds = aruco.refineDetectedMarkers(
        image=gray,
        board=board,
        detectedCorners=corners,
        detectedIds=ids,
        rejectedCorners=rejectedImgPoints,
        cameraMatrix=mtx,
        distCoeffs=dist,
    )
    retval, rvec, tvec = aruco.estimatePoseBoard(
        corners, ids, board, mtx, dist, rvec, tvec
    )
    if retval > 0:
        frame = aruco.drawAxis(frame, mtx, dist, rvec, tvec, markerWidth)
        frame = aruco.drawDetectedMarkers(frame, corners, ids)
    # Display the resulting frame
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
