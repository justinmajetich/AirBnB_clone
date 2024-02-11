#!/usr/bin/python3
"""1-pack_web_static module"""
from os.path import isfile
from datetime import datetime
from fabric.api import local


def do_pack():
    """Generates a .tgz archive from the contents of web_static folder of
    AriBnB Clone repo
    Returns: Archive path, otherwise False
    """
    ct = datetime.now().strftime("%Y%m%d%H%M%S")

    local("mkdir -p versions")

    local("tar -cvzf versions/web_static_{}.tgz web_static".format(ct))
    if isfile("versions/web_static_{}.tgz".format(ct)):
        return "versions/web_static_{}.tgz".format(ct)
