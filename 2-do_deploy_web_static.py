#!/usr/bin/python3
"""
This script creates a compressed archive of
a given folder and deploys it to web servers.
The archive is named based on the current date and time.
"""

import os
from fabric.api import local, env, put, run
from datetime import datetime


env.hosts = ['54.237.210.251', '54.237.14.69']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/*.pem'


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


def do_deploy(archive_path):
    """
    Distributes an archive to web servers and deploys it.

    Args:
        archive_path: The file path of the compressed archive to be deployed.

    Returns:
        True if all operations have been done correctly, False otherwise.
    """
    if not os.path.exists(archive_path):
        print("Archive not found at: {}".format(archive_path))
        return False

    file_name = archive_path.split("/")[-1]
    folder_name = "/data/web_static/releases/" + file_name[:-4]

    try:
        # Upload archive to server
        put(archive_path, "/tmp/")

        # Create directory to uncompress archive
        run("mkdir -p {}".format(folder_name))

        # Uncompress archive into folder
        run("tar -xzf /tmp/{} -C {}".
            format(file_name, folder_name))

        # Delete archive from server
        run("rm /tmp/{}".format(file_name))

        # Move contents of folder up one level
        run("mv {}/* {}".format(folder_name, folder_name + "/.."))

        # Remove empty folder
        run("rm -rf {}".format(folder_name))

        # Remove symbolic link
        run("rm -rf /data/web_static/current")

        # Create new symbolic link
        run("ln -s {} /data/web_static/current".format(folder_name + "/"))
        print("New version deployed!")
        return True

    except Exception as e:
        print("An unexpected error occurred: {}".format(str(e)))
        return False
