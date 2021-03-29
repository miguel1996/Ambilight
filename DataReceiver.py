import socket
import sys

host = "127.0.0.1"
port = 3000

try:
    receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver.bind((host, port))
    print("Listening on %s:%s" % (host, port))
except socket.error as err:
    print('Error: %s' % err)
    sys.exit()


while True:
    rawData, addr = receiver.recvfrom(1024)
    data = rawData.decode()
    print(data)
