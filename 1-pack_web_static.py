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
    archive_name = "web_static_{}.tgz".format(timestamp)
    archive_path = os.path.join("versions", archive_name)

    # Create 'versions' directory if it doesn't exist
    if not os.path.exists("versions"):
        os.mkdir("versions")

    # Create a .tgz archive of the web_static directory
    print("Packing web_static to {}".format(archive_path))
    result = local(
            "tar -cvzf {} web_static".format(archive_path),
            capture=False
            )

    if result.return_code == 0:
        size = os.path.getsize(archive_path)
        print("web_static packed: {} -> {}Bytes".format(archive_path, size))
        return archive_path
    else:
        return None
