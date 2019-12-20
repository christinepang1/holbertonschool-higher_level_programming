#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    sum = 0
    for i in set(my_list):
        sum += i
    return sum
