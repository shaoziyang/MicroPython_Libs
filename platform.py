

platform_pyb = 0
platform_esp = 0
def get_platform():
    global platform_pyb, platform_esp
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