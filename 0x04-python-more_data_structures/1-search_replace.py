#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list[:]
    for i in range(my_list.count(search)):
        new[new.index(search)] = replace
    return new
