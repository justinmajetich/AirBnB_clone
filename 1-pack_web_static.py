#!/usr/bin/python3
from fabric.api import run, local, put
from datetime import datetime
import os


def do_pack():
    """ fabric script that generates a .tgz """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(date)
    try:
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(path))
        return path
    except Exception:
        return None
