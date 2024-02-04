#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static """
from fabric.api import local
import time

a = time.strftime("%Y%m%d%H%M%S")


def do_pack():
    """ do_pack fonction """
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".format(a)
        return ("versions/web_static_{}.tgz".format(a)
    except:
        return None
