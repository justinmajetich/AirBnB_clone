#!/usr/bin/python3
"""
compress before sending
"""
from fabric.api import local
from datetime import datetime
import os
import tarfile


def do_pack():
    """generates an archive"""
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    path = local('mkdir -p versions')
    tar = local('tar -czvf versions/web_static_{}.tgz web_static'.format(now))
    if os.path.exists("/versions/web_static_{}.tgz".format(now)):
        return os.path.normpath("/versions/web_static_{}.tgz".format(now))
    else:
        return "None"
