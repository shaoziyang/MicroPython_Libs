
def isset(v): 
    try: 
        type (eval(v)) 
    except: 
        return 0 
    else: 
        return 1

