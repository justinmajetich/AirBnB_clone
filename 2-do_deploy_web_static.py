#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ["52.3.247.63", "54.234.100.112"]
env.user = "ubuntu"


def do_pack():
    """
        return the archive path if archive has generated correctly.
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_f_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_f_path))

    if t_gzip_archive.succeeded:
        return archived_f_path
    else:
        return None


def do_deploy(archive_path):
    """Distributes an archive to your web servers."""
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Uncompress the archive to the folder
        # /data/web_static/releases/<archive filename without extension>
        filename = os.path.basename(archive_path)
        dirname = "/data/web_static/releases/{}".format(filename.split('.')[0])
        run("mkdir -p {}".format(dirname))
        run("tar -xzf /tmp/{} -C {}".format(filename, dirname))
        run("rm /tmp/{}".format(filename))
        run("mv {}/web_static/* {}/".format(dirname, dirname))
        run("rm -rf {}/web_static".format(dirname))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create a new the symbolic link /data/web_static/current on the web server,
        # linked to the new version of your code (/data/web_static/releases/<archive filename without extension>)
        run("ln -s {} /data/web_static/current".format(dirname))

        # All operations have been done correctly
        return True

    except:
        # Something went wrong
        return False
