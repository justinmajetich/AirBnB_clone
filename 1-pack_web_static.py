#!/usr/bin/python3
from fabric.api import run, local, put
import datetime


def do_pack():
    """do pack method"""
    time = datetime.datetime.now()
    date = (str(time.year) + str(time.month) + str(time.day) + str(time.hour) +
            str(time.minute) + str(time.second))
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz ./web_static".format(date))
        return "./versions/web_static_{}.tgz".format(date)
    except:
        return None
    