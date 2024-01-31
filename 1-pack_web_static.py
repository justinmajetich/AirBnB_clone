#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive
from the contents of the web_static folder of
your AirBnB Clone repo, using the function do_pack
"""

from fabric.api import *
import os
from datetime import datetime


env.hosts = ['localhost']


def do_pack():
    """
    generates a .tgz archive
    from the contents of the web_static folder
    """

    pathname = '/versions/web_static_{}' + datetime.now().\
               strftime("%Y%m%d%H%M%S") + ".tgz"
    local("mkdir -p versions")

    local('tar -czvf archive_name.tgz /versions/web_static_\
          $(date +%Y%m%d%H%M%S).tgz\
    web_static')
    print("web_static packed: {} -> {}".
          format(pathname, os.path.getsize(pathname)))
