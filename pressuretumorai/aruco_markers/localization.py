import cv2

from markerGen import markerDict


def detectMarkers(frame):
    arucoParams = cv2.aruco.DetectorParameters_create()
    corners, ids, rejected = cv2.aruco.detectMarkers(
        frame, markerDict, parameters=arucoParams
    )
    if ids is not None:
        ids = ids.flatten()
        for (markerCorner, markerID) in zip(corners, ids):
            print(markerCorner)
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners
            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))
            cv2.line(frame, topLeft, topRight, (0, 255, 0), 2)
            cv2.line(frame, topRight, bottomRight, (0, 255, 0), 2)
            cv2.line(frame, bottomRight, bottomLeft, (0, 255, 0), 2)
            cv2.line(frame, bottomLeft, topLeft, (0, 255, 0), 2)
            cX = int((topLeft[0] + bottomRight[0]) / 2.0)
            cY = int((topLeft[1] + bottomRight[1]) / 2.0)
            cv2.circle(frame, (cX, cY), 4, (0, 0, 255), -1)
            # draw the ArUco marker ID on the image
            messageText = str(markerID) + " " + "(" + str(cX) + "," + str(cY) + ")"
            cv2.putText(
                frame,
                str(messageText),
                (topLeft[0], topLeft[1] - 15),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2,
            )
    return frame


def getFrames():
    videoObj = cv2.VideoCapture(1)
    while True:
        ret, frame = videoObj.read()
        cv2.imshow("Webcam Feed", detectMarkers(frame))
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    videoObj.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # getFrames()
    img = cv2.imread("/Users/aditya/Downloads/IMG_4572.JPG")
    cv2.imshow("Webcam Feed", detectMarkers(img))
    cv2.waitKey(0)
    # while True:
    #     cv2.imshow('WebFrame', detectMarkers(img))
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    cv2.destroyAllWindows()
