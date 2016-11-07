"""
File:     hts221.py
Desciipt: HTS221 Humidity and temperature micropython's I2C drive
Author:   shaoziyang
version:  2.0
Date:     2016 Nov
web:      http://www.micropython.org.cn/
github:   https://github.com/shaoziyang/MicroPython_Libs

License:  MIT

#usage:

from HTS221 import HTS221
ht = HTS221(i2c)
ht.get()

"""

from hal import hal_i2c
from micropython import const

DRV_VER   = 2.0
DRV_BUILD = 1010

# HTS221 I2C address
HTS_I2C_ADDR = const(0x5F)

# HTS221 register mapping
HTS221_WHO_AM_I     = const(0x0F)
HTS221_AV_CONF      = const(0x10)
HTS221_CTRL_REG1    = const(0x20)
HTS221_CTRL_REG2    = const(0x21)
HTS221_CTRL_REG3    = const(0x22)
HTS221_STATUS_REG   = const(0x27)
HTS221_HUMIDITY_OUT_L = const(0x28)
HTS221_HUMIDITY_OUT_H = const(0x29)
HTS221_TEMP_OUT_L   = const(0x2A)
HTS221_TEMP_OUT_H   = const(0x2B)
HTS221_H0_rH_x2     = const(0x30)
HTS221_H1_rH_x2     = const(0x31)
HTS221_T0_degC_x8   = const(0x32)
HTS221_T1_degC_x8   = const(0x33)
HTS221_T1T0_msb     = const(0x35)
HTS221_H0_T0_OUT_L  = const(0x36)
HTS221_H0_T0_OUT_H  = const(0x37)
HTS221_H1_T0_OUT_L  = const(0x3A)
HTS221_H1_T0_OUT_H  = const(0x3B)
HTS221_T0_OUT_L     = const(0x3C)
HTS221_T0_OUT_H     = const(0x3D)
HTS221_T1_OUT_L     = const(0x3E)
HTS221_T1_OUT_H     = const(0x3F)

class HTS221(object):
    def __init__(self, i2c):
        self.i2c = hal_i2c(i2c)
        self.ADDR = HTS_I2C_ADDR
        self.version = DRV_VER
        self.build = DRV_BUILD
        # HTS221 Temp Calibration registers
        self.T0_OUT = self.gr2(HTS221_T0_OUT_L)
        self.T1_OUT = self.gr2(HTS221_T1_OUT_L)
        if self.T0_OUT>=0x8000 :
            self.T0_OUT -= 65536
        if self.T1_OUT>=0x8000 :
            self.T1_OUT -= 65536
        t1 = self.gr(HTS221_T1T0_msb)
        self.T0_degC = (self.gr(HTS221_T0_degC_x8) + (t1%4)*256)/8
        self.T1_degC = (self.gr(HTS221_T1_degC_x8)+ ((t1%16)/4)*256)/8
        # HTS221 Humi Calibration registers
        self.H0_OUT = self.gr2(HTS221_H0_T0_OUT_L)
        self.H1_OUT = self.gr2(HTS221_H1_T0_OUT_L)
        self.H0_rH = self.gr(HTS221_H0_rH_x2)/2
        self.H1_rH = self.gr(HTS221_H1_rH_x2)/2
        # set av conf: T=4 H=8
        self.sr(HTS221_AV_CONF, 0x81)
        # set CTRL_REG1: PD=1 BDU=1 ODR=1
        self.sr(HTS221_CTRL_REG1, 0x85)

    # set register
    def sr(self, reg, dat):
        self.i2c.setReg(self.ADDR, reg, dat)

    # get one register
    def gr(self, reg):
        return self.i2c.getReg(self.ADDR, reg)

    # get two register
    def gr2(self, reg):
        return self.i2c.get2Reg(self.ADDR, reg)

    # Device identification
    def WhoAmI(self):
        return self.gr(HTS221_WHO_AM_I)

    # get STATUS regster
    def STATUS(self):
        return self.gr(HTS221_STATUS_REG)

    # power control
    def poweroff(self):
        t = self.gr(HTS221_CTRL_REG1) & 0x7F
        self.sr(HTS221_CTRL_REG1, t)

    def poweron(self):
        t = self.gr(HTS221_CTRL_REG1) | 0x80
        self.sr(HTS221_CTRL_REG1, t)

    # get/set Output data rate
    def ODR(self, ord=''):
        if ord != '':
            t = self.gr(HTS221_CTRL_REG1) & 0xFC
            self.sr(HTS221_CTRL_REG1, t | ord)
        else:
            return self.gr(HTS221_CTRL_REG1) & 0x03

    # get/set Humidity and temperature average configuratio
    def av(self, av=''):
        if av != '':
            self.sr(HTS221_AV_CONF, av)
        else:
            return self.gr(HTS221_AV_CONF)

    # calculate Temperature
    def getTemp(self):
        t = self.gr2(HTS221_TEMP_OUT_L)
        return self.T0_degC + (self.T1_degC - self.T0_degC) * (t - self.T0_OUT) / (self.T1_OUT - self.T0_OUT)

    # calculate Humidity
    def getHumi(self):
        t = self.gr2(HTS221_HUMIDITY_OUT_L)
        h = self.H0_rH + (self.H1_rH - self.H0_rH) * (t - self.H0_OUT) / (self.H1_OUT - self.H0_OUT)
        if h > 100:
            h = 100
        else:
            if h < 0:
                h = 0
        return h

    # get Humidity and Temperature
    def get(self):
        return [self.getHumi(), self.getTemp()]
