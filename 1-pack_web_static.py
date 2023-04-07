#!/usr/bin/python3
"""Creates a compressed archive of the web_static folder using its contents"""
from fabric.api import local, env
from datetime import datetime
import os

env.hosts = ['localhost']


def do_pack():
    """Creates a compressed archive of the web_static
      folder using its contents"""
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(now)
        local("tar -cvzf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except:
        return None
