#!/usr/bin/python3
""" using fabric"""
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """ pack all web_static"""
    time = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        time.year, time.month, time.day, time.hour,
        time.minute, time.second)
    try:
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(file))
        return file
    except:
        return None
