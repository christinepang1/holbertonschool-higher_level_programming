#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""


if __name__ == '__main__':
    import sys
    import requests

    if len(sys.argv) < 2:
        token = ""
    else:
        token = sys.argv[1]

    values = {'q': token}

    r = requests.post('http://0.0.0.0:5000/search_user', data=values)
    try:
        j_dict = r.json()
        if j_dict == {}:
            print('No result')
        else:
            print('[{}] {}'.format(j_dict['id'], j_dict['name']))
    except ValueError:
        print('Not a valid JSON')
