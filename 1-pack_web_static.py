#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static folder """

from fabric.api import local
from datetime import datetime


def do_pack():
    """ generates a .tgz archive from the contents of the web_static folder """
    try:
        local("mkdir -p versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file))
        return file
    except Exception:
        return None
