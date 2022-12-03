from picamera import PiCamera
from time import sleep

camera3= PiCamera()
camera_roatation = 180

camera3.preview_fullscreen=False
camera3.preview_window = (620, 320, 640, 480)

camera3.start_preview()
camera3.start_recording('/home/teamproject7/Desktop/Images.h264')
sleep(10)




camera3.stop_recording()
#camera3.stop_preview()