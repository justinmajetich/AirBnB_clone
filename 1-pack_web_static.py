#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of the
    web_static folder of AirBnB Clone version 2 repo, using the function
    do_pack."""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Function that generates a .tgz archive from the contents of the
    web_static folder"""
    if not os.path.isdir("versions"):
        if local("mkdir versions").failed:
            return None
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(date)
    try:
        print("Packing web_static to {}".format(file))
        local("tar -cvzf {} web_static".format(file))
        print("web_static packed: {} -> {}Bytes".format(
            file,
            os.path.getsize(file)
            )
            )
    except Exception:
        return None
    return file
