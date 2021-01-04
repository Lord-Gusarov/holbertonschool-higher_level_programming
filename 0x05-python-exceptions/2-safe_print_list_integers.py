#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    i = 0
    cnt_p = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            cnt_p += 1
            i += 1
        except IndexError as e:
            raise e
        except ValueError:
            i += 1
        except TypeError:
            i += 1
    print("")
    return cnt_p
