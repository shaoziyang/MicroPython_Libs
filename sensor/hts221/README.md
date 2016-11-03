#HTS221 I2C drive

Tested in CANNON board and ESP8266

The HTS221 is an ultra compact sensor for relative humidity and temperature. It includes a sensing element and a mixed signal ASIC to provide the measurement information through digital serial interfaces.

The sensing element consists of a polymer dielectric planar capacitor structure capable of detecting relative humidity variations and is manufactured using a dedicated ST process.

The HTS221 is available in a small top-holed cap land grid array (HLGA) package guaranteed to operate over a temperature range from -40 C to +120 C.

http://www.st.com/content/st_com/en/products/mems-and-sensors/humidity-sensors/hts221.html

Default device I2C address: 0x5F

-----

Author:  shaoziyang
version: 2.0
Date:    2016 Nov
web:     http://www.micropython.org.cn/
github:  https://github.com/shaoziyang/MicroPython_Libs

License: MIT

##usage

Basic usage:

    from HTS221 import HTS221
    ht = HTS221(i2c)
    ht.get()

other function:

    ht.getTemp()
    ht.getHumi()
    ht.poweroff()
    ht.poweron()

