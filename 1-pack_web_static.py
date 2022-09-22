#!/usr/bin/python3
# Fabfile that generates a .tgz archive from the contents of the web_static
from genericpath import isdir
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Create a .tgz archive of the local directory web_static
    """
    time = datetime.utcnow()
    filename = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        time.year,
        time.month,
        time.day,
        time.hour,
        time.minute,
        time.second)
    if os.path.isdir('versions') is False:
        if local('mkdir -p versions').failed is True:
            return None
    if local('tar -cvzf {} web_static'.format(filename)).failed is True:
        return None

    return filename
