import numpy as np
import cv2 as cv
import glob
import pickle

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6 * 9, 3), np.float32)
objp[:, :2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2)

# Arrays to store object points and image points from all the images.
objpoints = []  # 3d point in real world space
imgpoints = []  # 2d points in image plane.

images = glob.glob(
    "/Users/aditya/Programming/PressureTumorAI/pressuretumorai/calibration/dataset*.png"
)

for fname in images:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (9, 6), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners)
        # Draw and display the corners
        cv.drawChessboardCorners(img, (7, 6), corners2, ret)
        cv.imshow("img", img)
        cv.waitKey(100)
cv.destroyAllWindows()

[ret, mtx, dist, rvecs, tvecs] = cv.calibrateCamera(
    objpoints, imgpoints, gray.shape[::-1], None, None
)
pickle.dump(
    [ret, mtx, dist, rvecs, tvecs],
    open(
        "/Users/aditya/Programming/PressureTumorAI/data/cameraCoeffs.pickle",
        "wb",
    ),
)