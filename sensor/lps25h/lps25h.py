"""
File:     lps25h.py
Descript: LPS25H drive
Version:  2.0
Authur:   shaoziyang
Date:     2016.Nov

Usage:

from LPS25H import LPS25H
lps25=LPS25H(i2c)

# SA0 = 0
lps25=LPS25H(i2c, 0)

lps25.TEMP()
lps25.PRESS()
"""

from hal import hal_i2c

# device I2C addr
LPS25H_ADDR        = const(0x5C)

# register
LPS25H_REF_P_XL    = const(0x08)
LPS25H_REF_P_L     = const(0x09)
LPS25H_REF_P_H     = const(0x0A)
LPS25H_WHO_AM_I    = const(0x0F)
LPS25H_RES_CONF    = const(0x10)
LPS25H_CTRL_REG1   = const(0x20)
LPS25H_CTRL_REG2   = const(0x21)
LPS25H_CTRL_REG3   = const(0x22)
LPS25H_CTRL_REG4   = const(0x23)
LPS25H_INT_CFG     = const(0x24)
LPS25H_INT_SOURCE  = const(0x25)
LPS25H_STATUS_REG  = const(0x27)
LPS25H_POUT_XL     = const(0x28)
LPS25H_PRESS_OUT_L = const(0x29)
LPS25H_PRESS_OUT_H = const(0x2A)
LPS25H_TEMP_OUT_L  = const(0x2B)
LPS25H_TEMP_OUT_H  = const(0x2C)
LPS25H_FIFO_CTRL   = const(0x2E)
LPS25H_FIFO_STATUS = const(0x2F)
LPS25H_THS_P_L     = const(0x30)
LPS25H_THS_P_H     = const(0x31)
LPS25H_RPDS_L      = const(0x39)
LPS25H_RPDS_H      = const(0x3A)

class LPS25H(object):
    def __init__(self, i2c, SA0 = 1):
        self.i2c = hal_i2c(i2c)
        self.ADDR = LPS25H_ADDR | SA0
        # power on
        self.sr(LPS25H_CTRL_REG1, 0x90)

    def sr(self, reg, dat):
        self.i2c.setReg(self.ADDR, reg, dat)

    def gr(self, reg):
        return self.i2c.getReg(self.ADDR, reg)

    def gr2(self, reg):
        return self.i2c.get2Reg(self.ADDR, reg)

    # get Temperature
    def getTemp(self):
        t = self.gr2(LPS25H_TEMP_OUT_L)
        if t & 0x8000:
            t = t - 65536
        return 42.5 + t/480.0
        
    # get Pressure
    def getPress(self):
        return self.gr2(LPS25H_PRESS_OUT_L)/16

    # set power off
    def poweroff(self):
        t = self.gr(LPS25H_CTRL_REG1) & 0x7F
        self.sr(LPS25H_CTRL_REG1, t)

    # set power on
    def poweron(self):
        t = self.gr(LPS25H_CTRL_REG1) | 0x80
        self.sr(LPS25H_CTRL_REG1, t)

    # get/set Reference pressure
    def REF_PRESS(self, ref=''):
        if ref=='':
            return self.gr2(LPS25H_REF_P_L)
        else:
            self.sr(LPS25H_REF_P_L, ref%256)
            self.sr(LPS25H_REF_P_H, ref//256)

    # Device identification
    def WhoAmI(self):
        return self.gr(LPS25H_WHO_AM_I)

    # get/set Pressure and temperature resolution
    def RES_CONF(self, res=''):
        if res=='':
            return self.gr(LPS25H_RES_CONF)
        else:
            self.sr(LPS25H_RES_CONF, res)

    # get/set Control register 1
    def CTRL_REG1(self, reg=''):
        if reg=='':
            return self.gr(LPS25H_CTRL_REG1)
        else:
            self.sr(LPS25H_CTRL_REG1, reg)

    # get/set Control register 2
    def CTRL_REG2(self, reg=''):
        if reg=='':
            return self.gr(LPS25H_CTRL_REG2)
        else:
            self.sr(LPS25H_CTRL_REG2, reg)

    # get/set Control register 3
    def CTRL_REG3(self, reg=''):
        if reg=='':
            return self.gr(LPS25H_CTRL_REG3)
        else:
            self.sr(LPS25H_CTRL_REG3, reg)

    # get/set Control register 4
    def CTRL_REG4(self, reg=''):
        if reg=='':
            return self.gr(LPS25H_CTRL_REG4)
        else:
            self.sr(LPS25H_CTRL_REG4, reg)

    # get/set Interrupt configuration
    def INTERRUPT_CFG(self, cfg=''):
        if cfg=='':
            return self.gr(LPS25H_INT_CFG)
        else:
            self.sr(LPS25H_INT_CFG, cfg)

    # get/set Interrupt source
    def INT_SOURCE(self, src=''):
        if src=='':
            return self.gr(LPS25H_INT_SOURCE)
        else:
            self.sr(LPS25H_INT_SOURCE, src)

    # get Status register
    def STATUS(self):
        return self.gr(LPS25H_STATUS_REG)

    # get/set FIFO control
    def FIFO_CTRL(self, fifo=''):
        if fifo=='':
            return self.gr(LPS25H_FIFO_CTRL)
        else:
            self.sr(LPS25H_FIFO_CTRL, fifo)

    # get FIFO_STATUS
    def FIFI_STATUS(self):
        return self.gr(LPS25H_FIFO_STATUS)

    # get/set Threshold pressure
    def THS_PRESS(self, ths=''):
        if ths=='':
            return self.gr2(LPS25H_THS_P_L)
        else:
            self.sr(LPS25H_THS_P_L, ths%256)
            self.sr(LPS25H_THS_P_H, ths//256)
    
    # get/set Pressure offset
    def RPDS(self, rpds=''):
        if rpds=='':
            return self.gr2(LPS25H_RPDS_L)
        else:
            self.sr(LPS25H_RPDS_L, rpds%256)
            self.sr(LPS25H_RPDS_H, rpds//256)

