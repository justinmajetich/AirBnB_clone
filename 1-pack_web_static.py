#!/usr/bin/python3
"""creates .tgz archive from web_static folder using its contents"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """creates .tgz archive from web_static folder using its contents"""
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"web_static_{now}.tgz"
    local("mkdir -p versions")
    result = local(f"tar -czvf versions/{filename} web_static", capture=True)
    if result.failed:
        return None
    return f"versions/{filename}"