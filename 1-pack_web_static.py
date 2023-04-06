#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        # Create the versions directory if it doesn't exist
        local("mkdir -p versions")

        # Create the name of the archive
        now = datetime.now()
        archive_name = "web_static_{}{}{}{}{}{}.tgz"
        .format(now.year, now.month, now.day, now.hour, now.minute, now.second)

        # Create the tar command to compress the files
        tar_command = "tar -cvzf versions/{} web_static".format(archive_name)

        # Execute the tar command
        local(tar_command)

        # Return the archive path if the archive has been correctly generated
        return "versions/{}".format(archive_name)
    except Exception:
        # Return None if an error occurred
        return None

