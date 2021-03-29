import socket
import sys
import threading
from DataCollector import DataCollector

host = "127.0.0.1"
port = 3000

try:
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error as err:
    print('Error: %s' % err)
    sys.exit()

thread = threading.Thread(name='Color Update', target=DataCollector.update_color)
thread.start()

while True:
    data = DataCollector.get_color()

    try:
        sender.sendto(data.encode(), (host, port))

    except socket.error as err:
        print('Error: %s' % err)
        sys.exit()
