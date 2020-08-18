#!/usr/bin/env python3

"""
script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack
"""

from fabric.api import local
from os import path
from datetime import datetime


def do_pack():
    """
        script that generates a .tgz archive from
        the contents of the web_static folder of your
        AirBnB Clone repo, using the function do_pack.
    """
    local('mkdir -p versions')

    t = datetime.now()
    time = "{}{}{}{}{}{}".format(t.year, t.month,
                                 t.day, t.hour, t.minute,
                                 t.second)

    file_name = "web_static_{}.tgz".format(time)

    local('tar -czvf versions/{} web_static'.format(file_name))

    file_path = "versions/{}".format(file_name)
    if path.exists(file_path):
        return file_path
    else:
        return None
