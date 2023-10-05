#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
and deploys it using the function do_deploy.
"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ['54.172.84.26', '52.23.177.182']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    Distributes an archive to web servers and deploys it.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        archive_filename = os.path.basename(archive_path)
        archive_no_ext = os.path.splitext(archive_filename)[0]

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Create the release directory
        run("sudo mkdir -p /data/web_static/releases/{}"
            .format(archive_no_ext))

        # Uncompress the archive into the release directory
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(archive_filename, archive_no_ext))

        # Remove the uploaded archive
        run("sudo rm /tmp/{}".format(archive_filename))

        # Move the contents from the extracted folder to the release directory
        run("sudo mv /data/web_static/releases/{}/web_static/* \
/data/web_static/releases/{}/".format(archive_no_ext, archive_no_ext))

        # Remove the extracted folder
        run("sudo rm -rf /data/web_static/releases/{}/web_static"
            .format(archive_no_ext))

        # Remove the current symbolic link
        run("sudo rm -rf /data/web_static/current")

        # Create a new symbolic link to the new version
        run("sudo ln -s /data/web_static/releases/{} /data/web_static/current"
            .format(archive_no_ext))

        print("New version deployed!")
        return True

    except Exception as e:
        return False
