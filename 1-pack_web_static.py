#!/usr/bin/python3
"""
This script creates a compressed archive of a given folder.
The archive is named based on the current date and time.
"""

import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Compresses the web_static folder into a .tgz archive.

    The archive is stored in the versions folder and
    is named based on the current date and time.

    Returns:
        The file path of the compressed archive on success, None otherwise.
    """
    try:
        current_time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        file_name = "web_static_" + current_time + ".tgz"
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(file_name))
        archive_path = "versions/{}".format(file_name)
        return archive_path
    except OSError:
        print("An OS error occurred while creating the archive.")
        return None
    except Exception as e:
        print("An unexpected error occurred: {}".format(str(e)))
        return None
