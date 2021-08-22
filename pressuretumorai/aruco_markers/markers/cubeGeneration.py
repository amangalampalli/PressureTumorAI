import cv2
from cv2 import aruco

import numpy as np
from pressuretumorai.aruco_markers.markerGen import markerDict

board_ids = [0, 1, 2, 3, 4, 5]
markerWidth = 0.045
aruco_dict = markerDict
# Draw Paper Template for the board
def drawPaperTemplate():
    paperPxWidth = 300
    paperWidth = 0.2159 # This value is in meters, for 8.5x11" paper
    faceWidth  = 0.06   # This value is in meters
    cubeTemplate = np.ones((int(paperPxWidth*11/8.5),paperPxWidth))*255
    markerPx = int((markerWidth/paperWidth)*cubeTemplate.shape[1]/2)
    facePx   = int((faceWidth/paperWidth)*cubeTemplate.shape[1]/2)
    def drawMarkerAt(id, markerCenter):
        marker = aruco.drawMarker(aruco_dict, id, markerPx*2, borderBits=1)
        paddedMarker = np.ones((facePx*2, facePx*2))*255
        padding = facePx-markerPx
        paddedMarker[padding:(facePx*2)-padding,
                     padding:(facePx*2)-padding] = marker
        cv2.rectangle(paddedMarker, (0,0), (paddedMarker.shape[0]-1, paddedMarker.shape[1]-1), 0, 1)
        cubeTemplate[markerCenter[1] - facePx:markerCenter[1] + facePx,
                     markerCenter[0] - facePx:markerCenter[0] + facePx] = paddedMarker

    drawMarkerAt(board_ids[0], (int(cubeTemplate.shape[1]/2), facePx))
    drawMarkerAt(board_ids[1], (int(cubeTemplate.shape[1]/2), facePx + 1*facePx*2))
    drawMarkerAt(board_ids[2], (int(cubeTemplate.shape[1]/2) - facePx*2, facePx + 2*facePx*2))
    drawMarkerAt(board_ids[3], (int(cubeTemplate.shape[1]/2), facePx + 2*facePx*2))
    drawMarkerAt(board_ids[4], (int(cubeTemplate.shape[1]/2) + facePx*2, facePx + 2*facePx*2))
    drawMarkerAt(board_ids[5], (int(cubeTemplate.shape[1]/2), facePx + 3*facePx*2))
    return cubeTemplate

# Draw the paper template for the board
cv2.imshow('Template', cv2.resize(drawPaperTemplate(), None, fx=2, fy=2))
cv2.imwrite("/Users/aditya/Programming/PressureTumorAI/pressuretumorai/aruco_markers/markers/cubeNet.png", cv2.resize(drawPaperTemplate(), None, fx=2, fy=2))
while(not (cv2.waitKey(1) & 0xFF == ord('q'))):
   pass
cv2.destroyAllWindows()