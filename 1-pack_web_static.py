#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo.
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    # Create versions directory if not exist
    if not os.path.exists("./versions"):
        os.makedirs("./versions")

    # Create the archive filename with the current date and time
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_file = "versions/web_static_{}.tgz".format(now)

    try:
        print("Packing web_static to {}".format(archive_file))
        local("tar -cvzf {} web_static".format(archive_file))
        size = os.stat(archive_file).st_size
        print("web_static packed: {} -> {} Bytes".format(archive_file, size))
    except Exception:
        archive_file = None
    return archive_file
