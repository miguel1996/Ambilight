import socket
import sys
import threading
from ColorCollector import ColorCollector

host = "127.0.0.1"
port = 3000

try:
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error as err:
    print('Error: %s' % err)
    sys.exit()

colorCollector = ColorCollector()
colorCollector.set_sample(800, 600)

while True:
    try:
        threading.Thread(target=colorCollector.update_color(0)).start()
        sender.sendto(str(colorCollector.get_color()).encode(), (host, port))

    except socket.error as err:
        print('Error: %s' % err)
        sys.exit()
