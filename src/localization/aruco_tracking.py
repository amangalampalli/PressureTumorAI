import cv2
from src.localization.camera_init import *


def localization(frame, matList):
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
        corners, ids, board, mtx, dist, matList[0], matList[1]
    )
    if retval != 0:
        frame = aruco.drawAxis(frame, mtx, dist, rvec, tvec, markerWidth)
        frame = aruco.drawDetectedMarkers(frame, corners, ids)
        rMatrix = cv2.Rodrigues(rvec)[0]
        rotationTipMatrix = np.matmul(rMatrix, tipMatrix)
        return [
            np.ascontiguousarray(frame),
            np.add(rotationTipMatrix, np.transpose(tvec)[0]),
        ]
    else:
        return [
            np.ascontiguousarray(frame),
            np.zeros(
                3,
            ),
        ]


if __name__ == "__main__":
    l = [None, None]
    frame = cv2.imread("/Users/aditya/Programming/PressureTumorAI/image.jpg")
    res = localization(frame, l)
    print(res[1].shape)
