#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the
contents of the web_static folder and distributes it to web servers
"""
import os
from datetime import datetime

from fabric.api import env, local, put, run

env.hosts = ["34.234.193.86", "54.90.40.86"]


def do_pack():
    """Generates a .tgz archive from the contents of the web_static"""
    dt = datetime.now()
    file_name = "web_static_{}{}{}{}{}{}.tgz".format(
        dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
    )
    try:
        if not os.path.exists("versions"):
            os.mkdir("versions")
        local("tar -cvzf versions/{} web_static".format(file_name))
        return os.path.join("versions", file_name)
    except Exception:
        return None


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if os.path.exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(path, no_ext))
        run("tar -xzf /tmp/{} -C {}{}/".format(file_n, path, no_ext))
        run("rm /tmp/{}".format(file_n))
        run("mv {0}{1}/web_static/* {0}{1}/".format(path, no_ext))
        run("rm -rf {}{}/web_static".format(path, no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, no_ext))
        return True
    except Exception:
        return False
