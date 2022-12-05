#!/usr/bin/python

import threading
import sensors.PiMotor as PiMotor
import time
import RPi.GPIO as GPIO

class Motor:

    def __init__(self):
        self.forward_thread = threading.Thread(target=self.move_forward, args=(1,))
        self.backward_thread = threading.Thread(target=self.move_backward, args=(1,))
        self.left_thread = threading.Thread(target=self.move_left, args=(1,))
        self.right_thread = threading.Thread(target=self.move_right, args=(1,))
        self.thread_running = False
        self.thread_finished = False
        #Name of Individual MOTORS 
        self.m1 = PiMotor.Motor("MOTOR1",1)
        self.m2 = PiMotor.Motor("MOTOR2",1)
        self.m3 = PiMotor.Motor("MOTOR3",1)
        self.m4 = PiMotor.Motor("MOTOR4",1)

        #To drive all motors together
        self.motorAll = PiMotor.LinkedMotors(self.m1,self.m2,self.m3,self.m4)

        #Names for Individual Arrows
        self.ab = PiMotor.Arrow(1)
        self.al = PiMotor.Arrow(2)
        self.af = PiMotor.Arrow(3) 
        self.ar = PiMotor.Arrow(4)

    ##This segment drives the motors in the direction listed below:
    ## forward and reverse takes speed in percentage(0-100)

    def move_forward(self, name):
        print("Robot Moving Forward ")
        self.motorAll.forward(50)
        for i in range(20):
            if self.thread_running:
                time.sleep(0.1)
            else:
                break
        self.motorAll.stop()
        self.thread_finished = True

    def move_backward(self, name):
        print("Robot Moving Backward ")
        self.motorAll.reverse(100)
        for i in range(20):
            if self.thread_running:
                time.sleep(0.1)
            else:
                break
        self.motorAll.stop()
        self.thread_finished = True
    
    def move_left(self, name):
        print("Robot Moving Left ")
        self.m2.forward(100)
        self.m4.forward(100)
        for i in range(20):
            if self.thread_running:
                time.sleep(0.1)
            else:
                break
        self.m2.stop()
        self.m4.stop()
        self.thread_finished = True


    def move_right(self, name):
        print("Robot Moving Right ")
        self.m1.forward(100)
        self.m3.forward(100)
        for i in range(20):
            if self.thread_running:
                time.sleep(0.1)
            else:
                break
        self.m1.stop()
        self.m3.stop()
        self.thread_finished = True

    def stop_moving(self):
        self.motorAll.stop()