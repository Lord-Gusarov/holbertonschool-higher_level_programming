#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for x in names:
        if x[:2] != "__":
            print("{:s}".format(x))
