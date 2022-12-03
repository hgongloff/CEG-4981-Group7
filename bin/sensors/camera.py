import picamera as cam
import time as t
import os


class Camera:

    def __init__(self):
        self.camera = cam.PiCamera()
        self.camera.resolution = (640, 360)

    def take_picture(self):
        print("taking picture")
        os.chdir("/home/teamproject7/Pictures")
        self.camera.start_preview()
        t.sleep(2)
        self.camera.capture("test.jpg")
        self.camera.close()
