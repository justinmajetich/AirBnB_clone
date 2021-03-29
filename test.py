#!/usr/bin/python3

import sys
import shlex

string = sys.argv[1]
no_quote = shlex.split(string)

print(no_quote)
