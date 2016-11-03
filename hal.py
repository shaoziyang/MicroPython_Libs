'''
File:     hal.py
Descript: Hardware Abstraction Layer
Version:  1.0
Authur:   shaoziyang
Date:     2016 Nov
web:      http://www.micropython.org.cn/
github:   https://github.com/shaoziyang/MicroPython_Libs

License:  MIT

'''

import platform

version = 1.0
build   = 1100

class hal_i2c(object):
    def __init__(self, i2c):
        self.i2c = i2c
        platform.get_platform()
        if platform.platform_pyb:
            self.i2c_send = self.pyb_i2c_send
            self.i2c_recv = self.pyb_i2c_recv
        else:
            if platform.platform_esp:
                self.i2c_send = self.esp_i2c_send
                self.i2c_recv = self.esp_i2c_recv
            else:
                raise platform.PlatformError('unknow platform')

    # pyb i2c send
    def pyb_i2c_send(self, dev, buf):
        self.i2c.send(buf, dev)

    # pyb i2c recv
    def pyb_i2c_recv(self, dev, len):
        return self.i2c.recv(len, dev)

    # esp i2c send
    def esp_i2c_send(self, dev, buf):
        self.i2c.writeto(dev, buf)

    # esp i2c recv
    def esp_i2c_recv(self, dev, len):
        return self.i2c.readfrom(dev, len)

    # set a register
    def setReg(self, dev, reg, dat):
        self.i2c_send(dev, bytearray([reg, dat]))

    # get a register
    def getReg(self, dev, reg):
        self.i2c_send(dev, bytearray([reg]))
        t=self.i2c_recv(dev, 1)
        return t[0]

    # get two register
    def get2Reg(self, dev, reg):
        a = self.getReg(dev, reg)
        b = self.getReg(dev, reg + 1)
        return a + b * 256

