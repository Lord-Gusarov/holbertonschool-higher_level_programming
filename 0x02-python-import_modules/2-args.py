#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    cnt = len(args)
    if cnt == 1:
        print("0 arguments.")
    elif cnt == 2:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(cnt - 1))
    for i in range(1, cnt):
        print("{:d}: {:s}".format(i, args[i]))
