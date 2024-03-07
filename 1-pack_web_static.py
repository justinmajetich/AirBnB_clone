#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the
contents of the web_static folder
"""
import os
from datetime import datetime

from fabric.api import local


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    The archive is stored in the 'versions' folder.
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{timestamp}.tgz"
    archive_path = os.path.join("versions", archive_name)

    # Create 'versions' directory if it doesn't exist
    if not os.path.exists("versions"):
        os.mkdir("versions")

    # Create a .tgz archive of the web_static directory
    local(f"tar -cvzf {archive_path} web_static")

    return archive_path if os.path.exists(archive_path) else None
