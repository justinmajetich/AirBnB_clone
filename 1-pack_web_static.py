#!/usr/bin/python3
"""Fab script"""
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """Packs web_static into tgz"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_" + date + ".tgz"
    if os.isdir("versions") is False:
        local("mkdir -p versions")
    local("tar -cvzf " + file_name + " web_static")
    if os.path.exists(file_name):
        return file_name
    else:
        return None
