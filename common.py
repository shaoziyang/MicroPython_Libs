'''
File:     common.py
Descript: common functions
Version:  1.0
Authur:   shaoziyang
Date:     2016.Nov
web:      http://www.micropython.org.cn/
github:   https://github.com/shaoziyang/MicroPython_Libs

License:  MIT

'''

version = 1.0
build   = 1000

def isset(v):
    try:
        type (eval(v))
    except:
        return 0
    else:
        return 1

