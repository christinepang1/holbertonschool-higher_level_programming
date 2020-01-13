#!/usr/bin/python3
"""Text indentation module"""


def text_indentation(text):
    """
    Print a text with 2 new lines after . ? :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new = '\n\n'
    text = text.replace('.', '.' + new)
    text = text.replace('?', '?' + new)
    text = text.replace(':', ':' + new)

    print("\n".join([x.strip() for x in text.split("\n")]), end="")
