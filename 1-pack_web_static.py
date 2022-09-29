#!/usr/bin/python3
"""
Fabric file to generate a .tgz compresssed file for
the web_static directory
"""
from fabric.api import local
from datetime import datetime

def do_pack():
    curr_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "./versions/web_static_" + curr_datetime + ".tgz"
    local("mkdir -p ./versions")
    if local("tar -cvzf " + path + " ./web_static", capture = True).succeeded:
        return path
    return None
