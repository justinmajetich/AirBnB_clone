#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack."""
from fabric.api import local
from datetime import datetime

def do_pack():
    '''Function that generates a .tgz archive from the contents of the
    web_static folder.'''
    print("Packing web_static to versions/web_static_20170314233357.tgz")
    local('mkdir -p versions')
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file = f"versions/web_static_{date}.tgz"
    try:
        local(f'tar -cvzf {file} web_static')
        return file
    except:
        return None


