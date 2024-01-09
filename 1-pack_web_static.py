#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from contents of web_static."""
    time = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(time)
    try:
        local("mkdir -p ./versions")
        local("tar -czvf {} ./web_static".format(file_name))
    except Exception as e:
        print(e)
        return None
    else:
        return file_name
