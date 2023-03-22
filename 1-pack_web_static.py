#!/usr/bin/python3
"""
    Generate a .tgz archive from the contents of the web_static folder
    Function: do_pack():
    Folder: versions (should be created if it doesn't exist
    Name of archive: web_static_<year><month><day><hour><minute><second>.tgz
"""

from fabric.api import local
import time


def do_pack():
    """
        Generates a .tgz
        Return: archive path
    """
    time_now = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time_now))
        return ("versions/web_static_{}.tgz".format(time_now))
    except:
        return None
