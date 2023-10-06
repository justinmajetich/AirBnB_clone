#!/usr/bin/python3
"""
Compress "web_static" folder
"""
from fabric.decorators import task
from fabric.api import local
from datetime import datetime


@task
def do_pack():
    """Archive 'web_static' dir"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    arc_name = "web_static_{}.tgz".format(time)

    if local("tar -cvzf versions/{} web_static".format(arc_name)).succeeded:
        return "versions/{}".format(arc_name)
    return None
