#!/usr/bin/python3
"""
Compress before sending
"""

from os import path
from time import strftime
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Fabric script that generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo,
    using the function do_pack
    """

    archieve = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(archieve))

        return "versions/web_static_{}.tgz".format(archieve)

    except Exception:
        return None
