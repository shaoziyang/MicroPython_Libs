LPS25H micropython I2C drive for CANNON board

The LPS25H is an ultra compact absolute piezoresistive pressure sensor. It includes a monolithic sensing element and an IC interface able to take the information from the sensing element and to provide a digital signal to the external world.

http://www.st.com/content/st_com/en/products/mems-and-sensors/pressure-sensors/lps25h.html?icmp=pf255230_pron_pr_feb2014


Basic I2C address:
0x5C


Usage:

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

