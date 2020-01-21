#!/usr/bin/python3
"""Function that writes an object to a text file using JSON rep"""

import json


def save_to_json_file(my_obj, filename):
    """Writes object to text file"""
    with open(filename, mode='w') as f:
        f.write(json.dumps(my_obj))
