#!/usr/bin/python3
""" Fabric module """
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Archive the content of web_static folder"""
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_path = "versions/web_static_{}.tgz".format(time)
    cmd = "tar -cvzf {} web_static".format(file_path)
    local("mkdir -p versions")
    local(cmd)
    if os.path.exists(file_path):
        return file_path
    else:
        return None
