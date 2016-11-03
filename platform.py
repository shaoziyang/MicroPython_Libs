'''
File:     platform.py
Descript: get system platform
Version:  1.0
Authur:   shaoziyang
Date:     2016.Nov
web:      http://www.micropython.org.cn/
github:   https://github.com/shaoziyang/MicroPython_Libs

License:  MIT

Usage:

from platform

'''

version = 1.0
build   = 1100

platform_pyb = 0
platform_esp = 0
platform_esp32 = 0
platform_cc3200 = 0

# get current platform
def get_platform():
    global platform_pyb, platform_esp
    global platform_esp32, platform_cc3200

    try:
        import pyb
    except:
        pass
    else:
        platform_pyb = 1

    try:
        import esp
    except:
        pass
    else:
        platform_esp = 1

class PlatformError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
