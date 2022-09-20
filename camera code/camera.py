import numpy as np
import cv2
import v4l2py
import time
import subprocess
cap = cv2.VideoCapture(0) 
while(True):
    # Capture frame-by-frame
    subprocess.call(['v4l2-ctl -d /dev/video0 -c ircut=0'],shell=True)
    time.sleep(0.1)
    ret, frame = cap.read()
    cv2.imshow('Arducam ar1335 ircut=0',0)
    subprocess.call(['v4l2-ctl -d /dev/video0 -c ircut=1'],shell=True)
    time.sleep(0.1)
    ret, frame2 = cap.read()
    cv2.imshow('Arducam ar1335 ircut=1',0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Saving image...")
        cap.set(3,4160)  #set width
        cap.set(4,3120)  #set height
        time.sleep(0.1)
        subprocess.call(['v4l2-ctl -d /dev/video0 -c ircut=1'],shell=True)
        time.sleep(0.1)
        print("ircut=1")
        cap.grab()
        cap.grab()
        cap.grab()
        ret, frame = cap.read()
        cv2.imwrite("image_ircut_1.jpg",frame)
        subprocess.call(['v4l2-ctl -d /dev/video0 -c ircut=0'],shell=True)
        time.sleep(0.1)
        print("ircut = 0")
        cap.grab()
        cap.grab()
        cap.grab()
        cap.grab()
        cap.grab()
        ret,frame2 = cap.read()
        cv2.imwrite("image_ircut_0.jpg",frame2)
        break   
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()