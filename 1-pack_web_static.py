#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static folder
"""
from fabric.api import *
import time


def do_pack():
    timestr = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/\
                ".format(timestr))
        return "versions/web_static_{}.tgz".format(timestr)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
