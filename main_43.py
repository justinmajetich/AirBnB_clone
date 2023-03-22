#!/usr/bin/python3
""" Test
"""
from models.engine.file_storage import FileStorage
from inspect import isfunction


delete_fct = FileStorage.__dict__.get("delete")
if delete_fct is None:
    print("Missing public instance method `delete`")
    exit(1)

if not isfunction(delete_fct):
    print("`delete` is not a function")
    exit(1)

fs = FileStorage()
try:
    fs.delete()
    print("OK", end="")
except:
    print("`delete` is not a public instance method allowing no parameter")
    exit(1)