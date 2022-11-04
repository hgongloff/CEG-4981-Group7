"""Example of how to create a Peripheral device/GATT Server"""
# Standard modules
import logging
import random
import threading

# Bluezero modules
from bluezero import async_tools
from bluezero import adapter
from bluezero import peripheral

# constants
# Custom service uuid
CPU_TMP_SRVC = '12341000-1234-1234-1234-123456789abc'
# https://www.bluetooth.com/specifications/assigned-numbers/
# Bluetooth SIG adopted UUID for Temperature characteristic
CPU_TMP_CHRC = '2A6E'
# Bluetooth SIG adopted UUID for Characteristic Presentation Format
CPU_FMT_DSCP = '2904'


class CargoBotBle:

    def read_value(self):
        """
        Example read callback. Value returned needs to a list of bytes/integers
        in little endian format.

        This one does a mock reading CPU temperature callback.
        Return list of integer values.
        Bluetooth expects the values to be in little endian format and the
        temperature characteristic to be an sint16 (signed & 2 octets) and that
        is what dictates the values to be used in the int.to_bytes method call.

        :return: list of uint8 values
        """
        print("value read")
        cpu_value = random.randrange(3200, 5310, 10) / 100
        return list(int(cpu_value * 100).to_bytes(2,
                                                  byteorder='little', signed=True))

    def write_value(self, value, options):
        print('value written')
        print(value.decode())
        print(options)

    def update_value(self, characteristic):
        """
        Example of callback to send notifications

        :param characteristic:
        :return: boolean to indicate if timer should continue
        """
        print('updated value')
        # read/calculate new value.
        new_value = self.read_value()
        # Causes characteristic to be updated and send notification
        characteristic.set_value(new_value)
        # Return True to continue notifying. Return a False will stop notifications
        # Getting the value from the characteristic of if it is notifying
        return characteristic.is_notifying

    def notify_callback(self, notifying, characteristic):
        """
        Noitificaton callback example. In this case used to start a timer event
        which calls the update callback ever 2 seconds

        :param notifying: boolean for start or stop of notifications
        :param characteristic: The python object for this characteristic
        """
        if notifying:
            print('notified')
            async_tools.add_timer_seconds(2, self.update_value, characteristic)

    def broadcast(self, name):
        """Starts the bluetooth broadcast"""
        print("broadcast")
        print(name)
        self.cpu_monitor.publish()

    def __init__(self):
        adapter_address = list(adapter.Adapter.available())[0].address
        # threading.Thread.__init__(self)
        self.run_thread = threading.Thread(target=self.broadcast, args=(1,))
        """Creation of peripheral"""
        logger = logging.getLogger('localGATT')
        logger.setLevel(logging.DEBUG)
        # Example of the output from read_value
        print('CPU temperature is {}\u00B0C'.format(
            int.from_bytes(self.read_value(), byteorder='little', signed=True)/100))
        # Create peripheral
        self.cpu_monitor = peripheral.Peripheral(adapter_address,
                                                 local_name='Cargo Bot',
                                                 appearance=1344)
        # Add service
        self.cpu_monitor.add_service(srv_id=1, uuid=CPU_TMP_SRVC, primary=True)
        # Add characteristic
        self.cpu_monitor.add_characteristic(srv_id=1, chr_id=1, uuid=CPU_TMP_CHRC,
                                            value=[], notifying=False,
                                            flags=['read', 'write',
                                                   'write-without-response', 'notify'],
                                            read_callback=self.read_value,
                                            write_callback=self.write_value,
                                            notify_callback=self.notify_callback
                                            )
        # Add descriptor0
        self.cpu_monitor.add_descriptor(srv_id=1, chr_id=1, dsc_id=1, uuid=CPU_FMT_DSCP,
                                        value=[0x0E, 0xFE, 0x2F, 0x27, 0x01, 0x00,
                                               0x00],
                                        flags=['read'])
        # Publish peripheral and start event loop
        # cpu_monitor.publish()
