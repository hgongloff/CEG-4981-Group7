import picamera as cam
import time as t

camera=cam.PiCamera()
camera.resolution=(640,360)
camera.start_preview()
t.sleep(2)
camera.capture("test.jpg")
camera.close()