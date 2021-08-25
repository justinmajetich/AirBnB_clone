#!/usr/bin/python3
"""
    script generates a .tgz archive from the contents of the web_static folder
"""


from fabric.api import local
import time


def do_pack():
    """
        generates a .tgz archive from the contents of the web_static folder
    """
    try:
        now = time.strftime("%Y%m%d%H%M%S")
        name = "web_static_{:s}.tgz".format(now)
        path = "versions/{:s}".format(name)
        dest_path = "{:s}/".format("web_static")

        local("mkdir -p versions")
        local("tar -cvzf {:s} {}".format(path, dest_path))

        return path
    except Exception:
        return None
