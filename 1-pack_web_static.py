#!/usr/bin/python3
"""
Fabfile to generates a .tgz archive from
the contents of web_static written in python
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """pack all content within web_static
    into a .tgz archive
    The archive will be put in versions
    """
    if not os.path.exists("versions"):
        local("mkdir versions")
    now = datetime.now()
    name = "versions/web_static_{}.tgz".format(
        now.strftime("%Y%m%d%H%M%S")
    )
    cmd = "tar -cvzf {} {}".format(name, "web_static")
    result = local(cmd)
    if not result.failed:
        return name
