#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        (str): Archive path if successfully generated, None otherwise.
    """
    try:
        # Create the versions directory if it doesn't exist
        if not os.path.exists("versions"):
            local("mkdir -p versions")

        # Create the file name with current date and time
        current_time = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(current_time)

        # Create the .tgz archive
        local("tar -cvzf {} web_static".format(file_name))

        return file_name
    except Exception as e:
        return None
