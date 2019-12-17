#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = my_list[:]
    for i in range(len(new)):
        if idx < 0 or idx >= len(my_list):
            return m_list
        else:
            new[idx] = element
            return new
