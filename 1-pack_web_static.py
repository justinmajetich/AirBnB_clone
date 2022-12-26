#!/usr/bin/python3
# Compress before sending
from fabric.api import local
from datetime import datetime
<<<<<<< HEAD
import os


def do_pack():
    """script that generates .tgz archive"""
    folder = local('mkdir -p versions')
    date = datetime.now().strftime("%Y,%m,%d,%H,%M,%S")
    myVar = vars()
    archive = local('tar -cvzf versions/myVar["web_static_{}".format(date)] web_static')
    if os.path.exists('./versions/myVar["web_static_{}".format(date)]'):
        return os.path.normpath('versions/myVar["web_static_{}".format(date)]')
    else:
        return None
=======
from fabric.decorators import runs_once


@runs_once
def do_pack():
        """generates .tgz archive from the contents of the web_static folder"""
        local("mkdir -p versions")
        path = ("versions/web_static_{}.tgz"

.format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
        result = local("tar -cvzf {} web_static"
        .format(path))

        if result.failed:
            return None
        return path
>>>>>>> 225f16f056ed558794932de82bb4f0ec153f1a6b
