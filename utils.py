#!/usr/bin/python3
"""
module to define utils
"""
import re


def is_valid_param(param):
    """
    Function to check if a string matches the pattern
    Use re.match() to check if the string matches the pattern from the start
    """
    pattern = r'^[a-zA-Z0-9_]+=[a-zA-Z0-9_."@-]+$'
    return bool(re.match(pattern, param))


def parseArgs(args):
    """
    function to parse the args
    """
    splitedArgs = args.split()
    domainDict = {}

    for param in splitedArgs[1:]:
        if is_valid_param(param):
            key, value = param.split('=')
            value = parseValue(value)
            if value is None:
                continue
            domainDict[key] = value

    return splitedArgs[0], domainDict


def parseValue(val):
    """
    function to parse the value
    """
    if val is not None and val.strip() != "":

        if val[0] == "\"" and val[-1] == "\"":
            return parseString(val)

        elif '.' in val:
            try:
                val = float(val)
                return val
            except ValueError:
                pass

        else:
            try:
                val = int(val)
                return val
            except ValueError:
                pass


def parseString(val):
    result_string = val[1:-1].replace('"', '\\"')

    return result_string.replace('_', " ")
