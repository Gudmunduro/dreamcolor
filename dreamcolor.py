import socket

class Light():
    def __init__(self, ip, port=5000):
        self.ip   = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __send(self, msg):
        self.sock.sendto(bytearray(msg), (self.ip, self.port))

    def dim(self, a=10):
        """ Takes a number from 0-10 """

        self.__send([0x7e, 0x05, 0x03, 0x80 + a, 0x01, 0xff, 0xff, 0x00, 0xef])

    def rgb(self, r, g, b):
        """ Takes three numbers from 0-255 """

        self.__send([0x7e, 0x07, 0x05, 0x03, r, g, b, 0x00, 0xef])
