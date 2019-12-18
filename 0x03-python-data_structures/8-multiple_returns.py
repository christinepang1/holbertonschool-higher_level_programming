#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        letter = None
    else:
        letter = sentence[0]
    return len(sentence), letter
