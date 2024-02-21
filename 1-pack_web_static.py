#!/usr/bin/python3
"""
    This script  generates a .tgz archive from the contents of the web_static
    folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
        compresses web_static files into one file
    """
    local("mkdir -p versions")
    current_date = datetime.now().strftime("%Y%m%d%H%M%S")
    tar_path = "versions/web_static_{}.tgz".format(current_date)
    captured = local("tar -cvzf {} web_static".format(tar_path), capture=True)
    if captured.failed:
        return None
    return tar_path
