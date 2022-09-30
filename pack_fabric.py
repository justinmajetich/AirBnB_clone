#!/usr/bin/python3
"""
Module that contains a fabfile that archives the web_static folder
of the AirBnB Clone repo.
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """Archives the web_static folder """
    day = datetime.now()
    filename = "versions/web_static_{}{}{}\
{}{}{}.tgz".format(day.year, day.month, day.day,
                   day.hour, day.minute, day.second)
    local("mkdir -p versions")
    result = local(f"tar -cvzf {filename} web_static")

    if result.succeeded:
        return filename

    return None
