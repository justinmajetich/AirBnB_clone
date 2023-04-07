#!/usr/bin/env python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo.
"""
import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    try:
        # Create the versions directory if it doesn't exist
        if not os.path.isdir("versions"):
            os.mkdir("versions")
        # Create the filename using the current time
        now = datetime.now()
        filename = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second
        )

        # Compress the contents of the web_static folder
        local("tar -cvzf {} web_static".format(filename))

        # Return the path to the archive
        return "versions/{}".format(filename)
    except Exception:
        return None
