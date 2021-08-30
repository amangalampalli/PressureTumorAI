import cv2
import numpy as np

from TauLidarCommon.frame import FrameType
from TauLidarCamera.camera import Camera

camera = None

def initCamera():
    global camera
    port = None
    ports = Camera.scan()
    if len(ports) > 0:
        port = ports[0]
    camera = Camera.open(port)
    cameraInfo = camera.info()
    print("\nToF camera opened successfully:")
    print("    model:      %s" % cameraInfo.model)
    print("    firmware:   %s" % cameraInfo.firmware)
    print("    uid:        %s" % cameraInfo.uid)
    print("    resolution: %s" % cameraInfo.resolution)
    print("    port:       %s" % cameraInfo.port)

