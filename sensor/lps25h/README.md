LPS25H I2C drive

Tested in CANNON board and ESP8266

The LPS25H is an ultra compact absolute piezoresistive pressure sensor. It includes a monolithic sensing element and an IC interface able to take the information from the sensing element and to provide a digital signal to the external world.

http://www.st.com/content/st_com/en/products/mems-and-sensors/pressure-sensors/lps25h.html?icmp=pf255230_pron_pr_feb2014

default I2C address: 0x5C

---

Author:  shaoziyang

version: 2.0

Date:    2016 Nov

web:     http://www.micropython.org.cn/

github:  https://github.com/shaoziyang/MicroPython_Libs

License: MIT

##Usage:

for pyb:

    from pyb import I2C
    i2c = I2C(1, I2C.MASTER)

    from LPS25H import LPS25H
    lps25=LPS25H(i2c)

    lps25.TEMP()
    lps25.PRESS()


for esp8266:

    from machine import Pin, I2C
    i2c = I2C(Pin(14), Pin(2))

    from LPS25H import LPS25H
    lps25=LPS25H(i2c)

    lps25.TEMP()
    lps25.PRESS()


set I2C address SA0

    # SA0 = 0
    lps25=LPS25H(i2c, 0)

other function:

    lps25.CTRL_REG1()
    lps25.CTRL_REG2()
    lps25.CTRL_REG3()
    lps25.CTRL_REG4()
    lps25.RES_CONF()
    lps25.poweron()
    lps25.poweroff()
    lps25.INTERRUPT_CFG()
    lps25.INT_SOURCE()
    lps25.STATUS()
    lps25.FIFO_CTRL()
    lps25.FIFI_STATUS()
    lps25.THS_PRESS()
    lps25.RPDS()
    lps25.WhoAmI()

