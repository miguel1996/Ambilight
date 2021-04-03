import socket
import sys
from ColorCollector import ColorCollector

host = "127.0.0.1"
port = 3000

try:
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error as err:
    print('Error: %s' % err)
    sys.exit()

while True:
    data = ColorCollector.get_updated_color()

    try:
        sender.sendto(str(data).encode(), (host, port))

    except socket.error as err:
        print('Error: %s' % err)
        sys.exit()
