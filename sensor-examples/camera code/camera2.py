import picamera as cam
import picamera.array as ar
import cv2
camera2=cam.PiCamera()
camera2.resolution=(640,480)
capturing_camera=ar.PiRGBArray(camera2,size=(640,480))

for frame in camera2.capture_continuous(capturing_camera,format="bgr",use_video_port=True):
    img=frame.array
    cv2.imshow("Webcam",img)
    capturing_camera.truncate(0)

    if cv2.waitKey(10)==27:
        
        break