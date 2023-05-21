#!/usr/bin/python3
"""A Fabric script that archives the contents of web_static
into a tgz file"""

from datetime import datetime
from fabric.api import local
from os.path import isdir
import re
import tarfile


def do_pack():
    """distributes an archive to your web servers
    """
    target = local("mkdir -p versions")
    name = str(datetime.now()).replace(" ", '')
    opt = re.sub(r'[^\w\s]', '', name)
    tar = local('tar -cvzf versions/web_static_{}.tgz web_static'.format(opt))
    if os.path.exists("./versions/web_static_{}.tgz".format(opt)):
        return os.path.normpath("/versions/web_static_{}.tgz".format(opt))
    else:
        return None
