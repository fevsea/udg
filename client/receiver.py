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
        ser.write(b'hello')

    xbee = XBee(serial_port, callback=print_data)

    while True:
        try:
            time.sleep(0.01)
        except KeyboardInterrupt:
            break

    xbee.halt()
    serial_port.close()


def validate_pin(pinet):
    global base_url
    r = requests.post(base_url + "/pin/", json={"pin": pinet})
    return r.status_code


def processDoor(open):
    global base_url
    r = requests.post(base_url + "/pin/", json={"open": open})


def evaluatePin(pinR):
    status = validate_pin(pinR)
    if status == 403:
        return b'{"4":"KO"}'
    elif status == 200:
        return b'{"4":"OK"}'
    else:
        return None




def processData(line):
    out = None
    try:
        jsonD = json.loads(line)
        op = int(list(jsonD.keys())[0])
        if op == 1:
            processDoor(True)
        elif op == 2:
            processDoor(False)
        elif op == 3:
            out = evaluatePin(jsonD["3"])
    except:
        pass
    return out


def serialF():
    with serial.Serial('/dev/ttyUSB4', 9600) as ser:
        while True:
            line = ser.readline()
            print(line)
            out = None
            try:
                out = processData(line[:-2].decode("utf-8") )
            except:
                pass
            if out is not None:
                print(out)
                ser.write(out)

serialF()