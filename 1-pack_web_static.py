#!/usr/bin/python3
# makes tgz archive
import tarfile
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    # packs file
    try:
        name = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S")
        local('mkdir -p versions')
        local("tar -cvzf versions/{}.tgz {}".format(
            name, "web_static/"))
        size = os.path.getsize("./versions/{}.tgz".format(name))
        print("web_static packed: versions/{}.tgz -> {}Bytes".format(
            name, size))
    except:
        return None
