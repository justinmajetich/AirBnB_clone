#!/usr/bin/env python3
"""
Fabric script to distribute archive to web servers using do_deploy function
"""
import os
from fabric.api import env, put, run, local
from datetime import datetime


env.hosts = ['54.158.79.124', '54.146.64.149']
env.user = 'ubuntu'


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    try:
        if not os.path.exists("versions"):
            os.mkdir("versions")
        filename = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
        local("tar -czvf versions/{} web_static".format(filename))
        return "versions/{}".format(filename)
    except:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file, newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(newest_version, newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))
        print("New version deployed!")

        return True
    except:
        return False
