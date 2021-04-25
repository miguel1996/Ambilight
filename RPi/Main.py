import socket
import sys
import threading
import numpy

from LEDController import LEDController
from rpi_ws281x import *
from ast import literal_eval as make_tuple

host = "0.0.0.0"
port = 3000

try:
    receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver.bind((host, port))
    print("Listening on %s:%s" % (host, port))
except socket.error as err:
    print('Error: %s' % err)
    sys.exit()

ledController = LEDController()

while True:
    rawData, addr = receiver.recvfrom(1024)
    data = make_tuple(rawData.decode())
    threading.Thread(target=ledController.update_leds(Color(data[0], data[1], data[2]))).start()
    print(f'Data: {data}')
