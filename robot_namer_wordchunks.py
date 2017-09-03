#!/usr/bin/python

"""
Program for robot to name itself, by mallow
"""

import random

wordbits = [
    "mar",
    "zarg",
    "blag",
    "alph",
    "borg",
    "ka",
    "zed",
    "foo",
    "rug",
    "trubs",
    "nand",
    "plem",
    "miso",
    "alba",
    "ham",
    "mile",
    "rash",
    "iftill",
    "snaz",
    "ups",
    "dirz",
    "anst",
    "plum",
    "prim",
    "nozz",
    "whirl",
    "jick",
]

def wb():
    return random.choice(wordbits)

name = "%s%s %s%s" % (wb(), wb(), wb(), wb())
print(name)
