#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    datetime = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(datetime.year,
                                                         datetime.month,
                                                         datetime.day,
                                                         datetime.hour,
                                                         datetime.minute,
                                                         datetime.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
