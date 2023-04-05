#!/bin/python3
""" Fabric script that generates a .tgz archive from the contents of the
    web_static folder of AirBnB Clone version 2 repo, using the function
    do_pack."""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Function that generates a .tgz archive from the contents of the
    web_static folder"""
    if not os.path.exists("versions"):
        if local("mkdir -p versions").failed:
            return None
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(date)
    if local("tar -cvzf {} web_static".format(file)).failed:
        return None
    return file
