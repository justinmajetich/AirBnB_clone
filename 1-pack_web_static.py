#!/usr/bin/python3
""" Pack web static """
from fabric.api import local
import datetime


def do_pack():
    """ Fabric script that generates a .tgz archive """
    local("mkdir -p versions")
    date = datetime.datetime.now()
    format_time = date.strftime("%Y%m%d%H%M%S")
    new_file = local(
        "tar -cvzf versions/web_static_{}.tgz web_static".format(format_time))
    if new_file.succeeded:
        return "versions/web_static_{}.tgz web_static".format(format_time)
    else:
        return None