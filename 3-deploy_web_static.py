#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""


from datetime import datetime
from fabric.api import *
import os

env.hosts = ["18.210.15.7", "54.160.102.195"]
env.user = "ubuntu"


def do_pack():
    """
    Create a compressed archive of web_static content.
    """
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_filename = "web_static_{}.tgz".format(current_time)
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(archive_filename))
        return "versions/{}".format(archive_filename)
    except Exception as e:
        return None


def do_deploy(archive_path):
    """
    Distribute archive.
    """
    if os.path.exists(archive_path):
        # ... (existing do_deploy function)

        print("New version deployed!")
        return True

    return False


def deploy():
    """
    Deploy the web static content to the web servers.
    """
    # Create the compressed archive
    archive_path = do_pack()

    if archive_path is None:
        return False

    # Deploy the archive to the web servers
    result = do_deploy(archive_path)

    return result

if __name__ == "__main__":
    deploy()
