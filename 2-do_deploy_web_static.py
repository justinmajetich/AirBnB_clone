#!/usr/bin/python3
"""Deploy archive!"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        current_time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        file_name = "web_static_" + current_time + ".tgz"
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(file_name))
        return "versions/{}".format(file_name)
    except Exception as e:
        print(e)
        return None
