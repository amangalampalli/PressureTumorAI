from multiprocessing import Process
from pressuretumorai.pressure_sensing.web_server import startServer
from pressuretumorai.localization.stylus import showCamera
from pressuretumorai.utils.filewriter import closeFile

if __name__ == "__main__":
    try:
        serverProcess = Process(target=startServer)
        serverProcess.start()
        cameraPreview = Process(target=showCamera)
        cameraPreview.start()
        serverProcess.join()
        cameraPreview.join()
    except:
        closeFile()