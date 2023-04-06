#!/usr/bin/python3
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    and stores it in the versions directory.
    """
    try:
        # Create the versions directory if it doesn't exist
        local("mkdir -p versions")

        # Create the name of the archive with the current date and time
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(now)

        # Create the tar command to compress the files
        tar_command = "tar -czvf {} {}"
        .format(os.path.join("versions", archive_name), "web_static")

        # Execute the tar command
        local(tar_command)

        # Return the archive path if the archive has been correctly generated
        return os.path.join("versions", archive_name)

    except Exception as e:
        # Print the exception message and return None if an error occurred
        print("Error: {}".format(e))
        return None

