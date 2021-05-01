#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from contents of web_static"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    To geberate a tgz
    """
    now = datetime.now()
    path_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(now.year,
                                                              now.month,
                                                              now.day,
                                                              now.hour,
                                                              now.minute,
                                                              now.second)
    local("mkdir -p versions")
    file = local("tar -vczf {} web_static".format(path_file))
    if file.succeeded:
        return(path_file)
    else:
        return None
