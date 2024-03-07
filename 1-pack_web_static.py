#!/usr/bin/python3
"""
Fabfile to generates a .tgz archive from the contents
of web_static directory
"""
import os
from datetime import datetime

from fabric import Connection


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    # Create the versions directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Create a timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(timestamp)

    # Use tar to create the archive
    result = Connection("localhost").run(
            "tar -cvzf {} web_static".format(filename)
            )

    # Return the archive path if the archive was created successfully
    if result.ok:
        return filename
    else:
        return None
