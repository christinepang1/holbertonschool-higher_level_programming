#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list[:]
    for i in range(len(new)):
        if i == search:
            new[i] = replace
    return new
