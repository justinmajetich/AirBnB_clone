#!/usr/bin/python3
"""
Fabfile that creates a tgz archive from web_static
dir and places it in versions dir
"""
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Creates a .tgz archive from web_static dir and stored
    in dir versions
    """
    try:
        # create dir "versions" if it doesn't exist already
        local("mkdir -p versions")

        # create the name of the archive matching the template:
        # web_static_<year><month><day><hour><minute><second>.tgz
        current_time = datetime.now()
        date_stamp = current_time.strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_" + date_stamp
        full_archive_path = "versions/" + archive_name + ".tgz"

        # create the archive
        local("tar -czvf " + full_archive_path + " web_static")

        return full_archive_path

    except Exception:
        return None
