#!/usr/bin/python3
"""
This script creates an archive of a given folder
The script is run by the fabric library
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    The archive is named based on current date and time.

    Returns:
        Path to archive if created successfully
        None otherwise
    """
    try:
        current_time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        file_name = "web_static_" + current_time + ".tgz"
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(file_name))
        archive_path = "versions/{}".format(file_name)
        return archive_path
    Exception:
        return None
