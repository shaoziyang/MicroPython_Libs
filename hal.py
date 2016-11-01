import platform

class hal_i2c(object):
    def __init__(self, i2c):
        self.i2c = i2c
        platform.get_platform()
    
    def setReg(self, dev, reg, dat):
        if platform.platform_pyb:
            self.i2c.send(bytearray([reg, dat]), dev)
        else:
            if platform.platform_esp:
                self.i2c.writeto(dev, bytearray([reg, dat]))

    def getReg(self, dev, reg):
        if platform.platform_pyb:
            self.i2c.send(bytearray([reg]), dev)
            t=self.i2c.recv(1, dev)
        else:
            if platform.platform_esp:
                self.i2c.writeto(dev, bytearray([reg]))
                t=self.i2c.readfrom(dev, 1)
                return t[0]

    def get2Reg(self, dev, reg):
        a = self.getReg(dev, reg)
        b = self.getReg(dev, reg + 1)
        return a + b * 256

