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
    
    def temp(self, v=10):
        """ Takes a number from 0-10 """

        self.__send([0x7e, 0x05, 0x03, 0x80 + v, 0x02, 0xff, 0xff, 0x00, 0xef])

    def rgb(self, r, g, b, fade=True):
        """ Takes three numbers from 0-255 """

        fadeVal = 0x03 if fade else 0x04
        self.__send([0x7e, 0x07, 0x05, fadeVal, r, g, b, 0x00, 0xef])

    def brightness(self, a=100):
        """ Takes a number from 0-100 """

        self.__send([0x7e, 0x04, 0x01, a, 0xff, 0xff, 0xff, 0x00, 0xef])
    
    def preset(self, mode):
        """ Takes the id of the preset mode """

        self.__send([0x7e, 0x05, 0x03, mode, 0x03, 0xff, 0xff, 0x00, 0xef])
    
    def pattern(self, pattern_type, pattern):
        """ Takes the type and a list with rgb values like [r, g, b, r, g, b] etc """
        """
        Types:
        Jumping = 0
        Gradual = 1
        Strobe = 2
        """

        byte_list = [0xaf, 0x10, pattern_type, int(len(pattern))]
        for t in pattern:
            try:
                byte_list.append(t[0])
                byte_list.append(t[1])
                byte_list.append(t[2])
            except:
                print("Error: Adding values to byte list failed")
        self.__send(byte_list)
    
    def speed(self, s=200):
        """ Takes a number from 0 - 200 """

        self.__send([0x7e, 0x04, 0x02, s, 0xff, 0xff, 0xff, 0x00, 0xef])

    def on(self):
        """ Turns on the light """

        self.__send([0x7e, 0x04, 0x04, 0x01, 0xff, 0xff, 0xff, 0x00, 0xef])

    def off(self):
        """ Turns off the light """

        self.__send([0x7e, 0x04, 0x04, 0x00, 0xff, 0xff, 0xff, 0x00, 0xef])
