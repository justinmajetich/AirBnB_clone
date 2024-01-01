#!/usr/bin/env bash
"""
Fabric script locally deploys the AirBnB clone static page.
"""

from fabric.api import *
from fabric.operations import local, put, sudo
import os

def do_deploy(archive_path):
    """
    Distributes an archive to your web servers.

    Parameters:
        - archive_path (str): Path to the archive file.

    Returns:
        - True if deployment is successful, else False.
    """
    if os.path.isfile(archive_path) is False:
        return False

    try:
        archive = archive_path.split("/")[-1]
        path = "/data/web_static/releases"
        folder = archive.split(".")
        new_archive = ".".join(folder)

        # Create the release directory
        local("mkdir -p {}/{}/".format(path, folder[0]))

        # Extract the archive into the release directory
        local("tar -xzf ./versions/{} -C {}/{}/".format(new_archive, path, folder[0]))

        # Move the contents of web_static to the release directory
        local("mv {}/{}/web_static/* {}/{}/".format(path, folder[0], path, folder[0]))

        # Remove the web_static directory in the release directory
        local("rm -rf {}/{}/web_static".format(path, folder[0]))

        # Remove the existing /data/web_static/current symbolic link
        local("rm -rf /data/web_static/current")

        # Create a new symbolic link pointing to the new release directory
        local("ln -sf {}/{} /data/web_static/current".format(path, folder[0]))

    except Exception as e:
        print(e)
        return False
    finally:
        return True
