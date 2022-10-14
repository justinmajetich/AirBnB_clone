#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir
import sys


def do_hello():
    """generates a tgz archive"""
    # local("mkdir versions")
    local(" echo hello")


def myfunction(mystring):
    print(mystring)


if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])
