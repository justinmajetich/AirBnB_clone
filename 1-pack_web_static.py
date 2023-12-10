#!/usr/bin/python3
"""
script to generate a .tgz archive from the contents of the web_static folder.
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the web_static folder.
    """
    try:
        # Create versions folder if it doesn't exist
        local("mkdir -p versions")

        # Generate archive filename
        now = datetime.utcnow()
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second)

        # Create the .tgz archive
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the archive path if successful
        return os.path.join("versions", archive_name)
    except Exception:
        return None
