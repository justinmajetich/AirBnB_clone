#!/usr/bin/python3
"""
Fabric script that generates archive
"""

from fabric.api import *
from datetime import datetime
import os

env.hosts = ["18.232.52.73", "3.228.24.89"]
env.user = "ubuntu"


def do_pack():
    """
        return the archive path if correctly gernerated.
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
    """
        Distribute an archive to our web servers
    """
    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file,
                                             newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True

    return False


def deploy():
    """
    Deploy function do_pack and do_deploy.
    """
    path = do_pack()
    if path:
        do_deploy(path)
    return False


def do_clean(number=0):
    """Deletes out-of-date archives"""
    files = local("ls -1t versions", capture=True)
    file_names = files.split("\n")
    n = int(number)
    if n in (0, 1):
        n = 1
    for i in file_names[n:]:
        local("rm versions/{}".format(i))
    dir_server = run("ls -1t /data/web_static/releases")
    dir_server_names = dir_server.split("\n")
    for i in dir_server_names[n:]:
        if i is 'test':
            continue
        run("rm -rf /data/web_static/releases/{}"
            .format(i))
