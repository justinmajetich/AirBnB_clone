#!/usr/bin/python3
# Compress before sending
from fabric.api import local
from datetime import datetime
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
