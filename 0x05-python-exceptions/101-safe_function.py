#!/usr/bin/python3


def safe_function(fct, *args):
    import sys
    r = None
    try:
        r = fct(*args)
    except:
        print("Exception:", sys.exc_info()[1], file=sys.stderr)
    return r
