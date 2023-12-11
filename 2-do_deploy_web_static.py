#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ["18.210.15.7", "54.160.102.195"]
env.user = "ubuntu"

@task
def do_deploy(archive_path):
    """
    Distribute archive.
    """
    if os.path.exists(archive_path):
        # Extracting necessary information from the archive_path
        archived_file = archive_path.split("/")[-1]
        filename_no_ext = os.path.splitext(archived_file)[0]

        # Remote paths on the server
        newest_version = "/data/web_static/releases/" + filename_no_ext
        archived_file_remote = "/tmp/" + archived_file

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Uncompress the archive to the folder
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file_remote,
                                             newest_version))

        # Delete the archive from the web server
        run("sudo rm {}".format(archived_file_remote))

        # Move content to the correct location
        run("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))

        # Remove unnecessary directory
        run("sudo rm -rf {}/web_static".format(newest_version))

        # Delete the symbolic link /data/web_static/current from the web server
        run("sudo rm -rf /data/web_static/current")

        # Create a new symbolic link /data/web_static/current on the web server
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True

    return False
