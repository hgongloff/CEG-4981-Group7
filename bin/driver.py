from cargo_bot import CargoBot
import RPi.GPIO as GPIO
import sys


if __name__ == '__main__':
    cargo_bot = CargoBot()
    exit_command = False

    while (not exit_command):
        print("Please issue a message. \n Type '1' to play alarm\
                  \n Type '2' to connect to ble mobile device\
                  \n Type '3' to send test message to mobile device \
                  \n Type '4' to request message from mobile device \
                  \n Type '5' to get weight sensor data \
                  \n Type '6' to get distance sensor data \
                  \n Type '7' to get a picture with the camera\
                  \n Type '8' to move forward for one second\
                  \n Type '9' to stop ble thread \
                  \n or type 'q' to quit")

        command = input("")
        if (command == ('q')):
            exit_command = True
            GPIO.cleanup()
            print("cleaned up GPIO")
            print("Exiting program")
            cargo_bot.stop_threads()
            sys.exit()

        elif (command == ('1')):
            cargo_bot.play_alarm()

        elif (command == ('2')):
            cargo_bot.connect_to_phone()

        elif (command == ('3')):
            cargo_bot.send_message()

        elif (command == ('4')):
            cargo_bot.get_message()

        elif (command == ('5')):
            cargo_bot.get_weight()

        elif (command == ('6')):
            cargo_bot.get_distance()

        elif (command == ('7')):
            cargo_bot.get_picture()

        elif (command == ('8')):
            cargo_bot.move_forward()

        elif (command == ('9')):
            cargo_bot.stop_threads()
        