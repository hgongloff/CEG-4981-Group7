from cargo_bot import CargoBot


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

        elif (command == ('1')):

            CargoBot.play_alarm()

        elif (command == ('2')):
            CargoBot.connect_to_phone()

        elif (command == ('3')):
            CargoBot.send_message()

        elif (command == ('4')):
            CargoBot.get_message()
