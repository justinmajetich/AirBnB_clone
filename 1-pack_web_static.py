#!/usr/bin/python3
"""A module for Fabric script that generates a .tgz archive."""
import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """Archives the static files."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    d_time = datetime.now()
    formatted_month = "{:02d}".format(d_time.month)
    formatted_day = "{:02d}".format(d_time.day)
    formatted_hour = "{:02d}".format(d_time.hour)
    formatted_minute = "{:02d}".format(d_time.minute)
    formatted_second = "{:02d}".format(d_time.second)
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        d_time.year,
        formatted_month,
        formatted_day,
        formatted_hour,
        formatted_minute,
        formatted_second
    )
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, size))
    except Exception:
        output = None
    return output
