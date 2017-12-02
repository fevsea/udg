import serial
import time
from xbee import XBee
import serial
import time
from xbee import XBee

import requests
import json
from collections import OrderedDict

base_url = "http://ec2-18-194-197-28.eu-central-1.compute.amazonaws.com"


def receive_xbee_pin():
    PORT = '/dev/ttyUSB4'
    BAUD_RATE = 9600
    serial_port = serial.Serial(PORT, BAUD_RATE)

    def print_data(data):
        """
        This method is called whenever data is received
        from the associated XBee device. Its first and
        only argument is the data contained within the
        frame.
        """
        print(data)

    xbee = XBee(serial_port, callback=print_data)

    while True:
        try:
            time.sleep(0.01)
        except KeyboardInterrupt:
            break

    xbee.halt()
    serial_port.close()


def validate_pin(pinet):
    # TODO
    global base_url
    r = requests.post(base_url + "/pin/", json={"pin": pinet})
    if r.status_code == 403:
        print("Unauthorized")
    elif r.status_code == 200:
        print("Okok")
    else:
        print("Unhandled error")

def serialF():
    with serial.Serial('/dev/ttyUSB4', 9600) as ser:
        while True:
            line = ser.readline()
            print(line)

serialF()