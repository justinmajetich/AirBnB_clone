#!/usr/bin/python3
"""
module - creating a .tgz archive from contents of web_static
folder using do_pack.
"""


from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """pack files of web_static folder into .tgz archive"""

    try:
        path = "versions"
        # if not os.path.exists(path):
        #     os.makedirs(path)
        #  or
        if os.path.isdir(path) is False:
            local("mkdir versions")  # create folder versions
        now = datetime.now()
        date = now.strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(date)
        command = "tar -cvzf {} web_static".format(file_name)
        local(command)
        return file_name
    except:
        return None