#!/usr/bin/python3
"""
Fabfile that generates a .tgz archive from the contents of web_static folder.
"""
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Creates a tgz archive from the contents of web_static.

    Returns:
        Archive path, otherwise None
    """
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    print("Packing web_static to {}".format(file))
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    print("web_static packed: {} -> {}Bytes".format(
        file,
        os.path.getsize(file)
        )
    )
    return file
