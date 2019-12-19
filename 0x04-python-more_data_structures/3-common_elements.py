#!/usr/bin/python3
def common_elements(set_1, set_2):
    _a = set(set_1)
    _b = set(set_2)
    if _a & _b:
        return _a & _b
