#!/usr/bin/python3
"""Function that creates an object from a "JSON file": """

import json


def load_from_json_file(filename):
    """Creates object from filename"""
    with open(filename, mode='r') as f:
        return json.load(f)
