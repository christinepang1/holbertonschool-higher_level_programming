#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    sum = my_list[0]
    for i in range(len(my_list) - 1):
        if (my_list[i] != my_list[i+1]):
            sum += my_list[i+1]
    return sum