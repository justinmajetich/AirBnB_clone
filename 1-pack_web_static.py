#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive from the
contents of the web_static folder of your
AirBnB Clone repo, using the function do_pack."""
from fabric.api import local
from datetime import datetime
from os import path


def do_pack():
    """Prototype: def do_pack():"""
    try:
        if not path.exists("versions"):
            local('mkdir versions')
        created_time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_path = "versions/web_static_{}.tgz".format(created_time)
        local("tar -cvzf {} web_static".format(file_path))
        return file_path
    except Exception:
        return None
