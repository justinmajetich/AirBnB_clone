#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents
# of the web_static folder of your AirBnB Colne repo,
# using the function do_pack
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    that fenerates a .tgz archive from the contents of the web_static folder
    """
    dt = datetime.utcnow()
    file = "versions/web_statis_{}{}{}{}{}{}.tgz".fotmat(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is false:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
