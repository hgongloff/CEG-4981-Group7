import picamera as cam
import time as t

camera=cam.PiCamera()
camera.resolution=(640,360)
camera.start_preview()
t.sleep(2)
camera.capture("12_4_22_test_pic.jpg")
camera.close()