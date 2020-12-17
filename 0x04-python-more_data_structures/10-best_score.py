#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    bk = None
    if len(a_dictionary) > 0:
        pairs = list(a_dictionary.items())
        bk, bv = pairs[0]
        for k, v in pairs:
            if v > bv:
                bk = k
                bv = v
    return bk
