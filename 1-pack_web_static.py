#!/usr/bin/python3
""" This Fabric script generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack."""
from fabric.operations import local
from datetime import datetime


def do_pack():
    """ All archives must be stored in the folder versions
    (your function should create this folder if it doesn’t exist) """
    local("mkdir -p versions")
    status = local("tar -cvzf versions/web_static_{}.tgz web_static"
                   .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                   capture=True)
    if status.failed:
        return None
    print(status)
    return status
