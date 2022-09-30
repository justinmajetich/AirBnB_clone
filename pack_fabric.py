#!/usr/bin/python3
"""
Module that contains a fabfile that archives the web_static folder
of the AirBnB Clone repo.
"""
from datetime import datetime
from fabric.api import local

from fabric.decorators import runs_once

@runs_once
def do_pack():
    """Archives the web_static folder """
    filename = ("versions/web_static_{}.tgz"
                .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    local("mkdir -p versions")
    result = local(f"tar -cvzf {filename} web_static")

    if result.succeeded:
        return filename

    return None
