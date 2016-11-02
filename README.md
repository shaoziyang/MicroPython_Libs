#MicroPython_Libs

Micropython libraries for a wide variety of modules, components, sensors.

Main purpose is let drive compatible with the esp8266 and pyb architectures, make it easy to use.

Library will be continuous renewal.



#Usage:

- for pyb

    from pyb import I2C
    i2c = I2C(1, I2C.MASTER)

    from LPS25H import LPS25H
    lps25=LPS25H(i2c)

    lps25.TEMP()
    lps25.PRESS()


- for esp8266:

    from machine import Pin, I2C
    i2c = I2C(Pin(14), Pin(2))

    from LPS25H import LPS25H
    lps25=LPS25H(i2c)

    lps25.TEMP()
    lps25.PRESS()
