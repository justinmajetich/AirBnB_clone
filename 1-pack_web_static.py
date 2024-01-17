#!/usr/bin/python3
#
from fabric.api import task, local
from datetime import datetime


@task
def do_pack():
    """
    Generates a .tgz archive from the
    contents of the web_static folder
    """
    local("mkdir -p versions")
    t = datetime.now()
    t = t.strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(t)
    try:
        local("tar -cvzf {} web_static".format(path))
        return path
    except Exception:
        return None
