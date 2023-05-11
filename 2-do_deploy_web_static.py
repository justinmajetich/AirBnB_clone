#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers using the function do_deploy:

    Prototype: def do_deploy(archive_path):
    Returns False if the file at the path archive_path doesn’t exist
    The script should take the following steps:
        Upload the archive to the /tmp/ directory of the web server
        Uncompress the archive to the folder
          /data/web_static/releases/<archive filename without extension>
          on the web server
        Delete the archive from the web server
        Delete the symbolic link /data/web_static/current from the web server
        Create a new symbolic link /data/web_static/current on the web server,
          linked to the new version of your code
          (/data/web_static/releases/<archive filename without extension>)
    All remote commands must be executed on your both web servers:
      (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
    Returns True if all operations are done correctly, otherwise returns False
    You must use this script to deploy it on your servers:
      xx-web-01 and xx-web-02
"""
from fabric.api import *
import os.path


env.hosts = ['34.234.193.7', '54.174.67.136']
env.user = "ubuntu"


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""

    if not os.path.isfile(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        # Uncompress the archive to the folder
        archive_filename = os.path.basename(archive_path)
        archive_name = os.path.splitext(archive_filename)[0]
        run("sudo mkdir -p /data/web_static/releases/{}/"
            .format(archive_name))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(archive_filename, archive_name))

        # Delete the archive from the web server
        run("sudo rm /tmp/{}".format(archive_filename))

        # Move files from archive to the right path
        run("sudo mv /data/web_static/releases/{}/web_static/* \
           /data/web_static/releases/{}/".format(archive_name, archive_name))

        run("sudo rm -rf /data/web_static/releases/{}/web_static"
            .format(archive_name))

        # Delete symbolic link /data/web_static/current from the web server
        run("sudo rm -rf /data/web_static/current")

        # Create new symbolic link /data/web_static/current on the web server
        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(archive_name))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Error: {}".format(e))
        return False
