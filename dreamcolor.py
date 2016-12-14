import socket

class Light():
    def __init__(self, ip, port=5000, broadcast=False):
        self.ip   = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if broadcast:
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    def __send(self, msg):
        self.sock.sendto(bytearray(msg), (self.ip, self.port))

    def dim(self, a=10):
        """ Takes a number from 0-10 """

        self.__send([0x7e, 0x05, 0x03, 0x80 + a, 0x01, 0xff, 0xff, 0x00, 0xef])

    def rgb(self, r, g, b, fade=True):
        """ Takes three numbers from 0-255 """

        fadeVal = 0x03 if fade else 0x04
        self.__send([0x7e, 0x07, 0x05, fadeVal, r, g, b, 0x00, 0xef])

    def on(self):
        """ Turns on the light """

        self.__send([0x7e, 0x04, 0x04, 0x01, 0xff, 0xff, 0xff, 0x00, 0xef])

    def off(self):
        """ Turns off the light """

        self.__send([0x7e, 0x04, 0x04, 0x00, 0xff, 0xff, 0xff, 0x00, 0xef])
