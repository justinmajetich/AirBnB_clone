#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the
   contents of the web_static folder
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """Generates a .tgz archive from the contents of
       the web_static folder of your AirBnB Clone repo
    """
    local("mkdir -p versions")
    created_at = datetime.now().strftime("%Y%m%d%H%M%S")
    # From the archive path and command
    arch_path = "versions/web_static_{}.tgz".format(created_at)
    command = "tar -cvzf {} web_static".format(arch_path)
    try:
        # perform fab command
        local(command)
        return arch_path
    except Exception as e:
        return None
