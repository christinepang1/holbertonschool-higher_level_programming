#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    this = list(a_dictionary.keys())[0]
    for keys in a_dictionary.keys():
        if a_dictionary[keys] > a_dictionary[this]:
            this = keys
    return this
