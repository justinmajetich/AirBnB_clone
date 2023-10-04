#!/usr/bin/python3
"""Fabric script that compresses my static files with gzip """

from fabric.api import task, local
from datetime import datetime as stamp


@task(alias="pack")
def do_pack():
    """Function that returns a gzip compressed file"""
    try:
        path = f"versions/web_static_{stamp.now().strftime('%Y%m%d%H%M%S')}.tgz"
        local("mkdir -p versions")
        local(f"tar -cvzf {path} web_static")
    except:
        return None
    else:
        return path
