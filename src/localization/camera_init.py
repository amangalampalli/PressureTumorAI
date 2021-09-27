import cv2
from cv2 import aruco
from src.data_generation.aruco.marker_generation import markerDict
import numpy as np
import pickle

ret, mtx, dist, rvecs, tvecs = pickle.load(
    open("/Users/aditya/Programming/PressureTumorAI/data/cameraCoeffs.pickle", "rb")
)

aruco_dict = markerDict
parameters = aruco.DetectorParameters_create()
parameters.cornerRefinementMethod = aruco.CORNER_REFINE_SUBPIX

markerWidth = 0.0508
tipMatrix = np.array([0.13, 0.0, 0.0])

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
