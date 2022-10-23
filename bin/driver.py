from cargo_bot import CargoBot
import sys


if __name__ == '__main__':
    cargo_bot = CargoBot()
    exit_command = False

    while (not exit_command):

        print("Please issue a message. \n Type '1' to play alarm\
                  \n Type '2' to connect to ble mobile device\
                  \n Type '3' to send test message to mobile device \
                  \n Type '4' to request message from mobile device \
                  \n or type 'q' to quit")

        command = input("")
        if (command == ('q')):
            exit_command = True
            sys.exit()

        elif (command == ('1')):
            cargo_bot.play_alarm()

        elif (command == ('2')):
            cargo_bot.connect_to_phone()

        elif (command == ('3')):
            cargo_bot.send_message()

        elif (command == ('4')):
            cargo_bot.get_message()
