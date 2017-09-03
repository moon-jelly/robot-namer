#!/usr/bin/python

"""
Program for robot to name itself, by mallow
"""

import random

with open("/usr/share/dict/propernames", "r") as f:
    names = f.read().splitlines(False)

with open("/usr/share/dict/words", "r") as f:
    words = f.read().splitlines(False)

name = "%s %s" % (random.choice(names), random.choice(words).capitalize())

print(name)
