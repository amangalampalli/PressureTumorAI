# from multiprocessing import Process
# from pressuretumorai.pressure_sensing.web_server import startServer
# from pressuretumorai.localization.stylus import showCamera
# from pressuretumorai.utils.filewriter import closeFile

# if __name__ == "__main__":
#     try:
#         serverProcess = Process(target=startServer)
#         serverProcess.start()
#         cameraPreview = Process(target=showCamera)
#         cameraPreview.start()
#         serverProcess.join()
#         cameraPreview.join()
#     except:
#         closeFile()

import cv2
from src.localization.stylus import processFrame
from src.web_server.web_server import initSocket, runServer
from src.data_processing.filewriter import writeFile, closeFile

if __name__ == "__main__":
    connection, client_address = initSocket()
    while True:
        frame = processFrame(findPosition=False)
        message = runServer(connection, client_address)
        if message is not None:
            writeFile(str(processFrame(findPosition=True)) + ", " + str(message))
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    closeFile()
