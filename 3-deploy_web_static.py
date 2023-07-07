#!/usr/bin/python3
"""

"""

from datetime import datetime
from fabric.api import *
import os

env.user = "ubuntu"
env.hosts = ['54.197.44.197', '34.207.227.83']


def do_pack():
    """
    Returns the archive path if archive has been
    correctly gernerated else return None
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_pathh = "versions/web_static_{}.tgz".format(date)
    tgz_archive = local("tar -cvzf {} web_static".format(archive_pathh))

    if tgz_archive.succeeded:
        return archive_pathh
    else:
        return None


def do_deploy(archive_path):
    """
    """
    if os.path.exist(archive_path):
        archive_file = archive_path[9:]
        archiveFilePath = "/tmp/" + archive_file

        put(archive_path, "/tmp/")

        newRemotePath = "/data/web_static/releases/" + archive_path[:-4]
        run("sudo mkdir -p {}".format(newRemotePath))

        run("sudo tar -xzvf {} -C {}/".format(archiveFilePath, newRemotePath))
        run("sudo rm -rf {}".format(archiveFilePath))
        run("sudo mv {}/web_static/* {}".format(newRemotePath,
                                                newRemotePath))

        run("sudo rm -rf {}/web_static".format(newRemotePath))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newRemotePath))
        print("Success")
        return True
    else:
        return False

def deploy():
    """
    creates and distributes an archive to your web servers
    """
    path = do_pack
    if path:
        do_deploy(path)
    else:
        return False
