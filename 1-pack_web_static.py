#!/usr/bin/python3
"""Archiving a folder using fabric api"""


from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """Generate a .tgz archive from
the contents of web_static folder"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        fileName = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(fileName))
        return fileName
    except:
        return None
