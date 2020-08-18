#!/usr/bin/python3

"""
script that distributes an archive to your web servers
using the function do_deploy
"""

from fabric.api import *
from os.path import isfile, exists
from datetime import datetime

env.hosts = ['34.73.51.195', '34.73.59.80']


def do_pack():
    """
        script that generates a .tgz archive from
        the contents of the web_static folder of your
        AirBnB Clone repo, using the function do_pack.
    """
    local('mkdir -p versions')

    t = datetime.now()
    time = "{}{}{}{}{}{}".format(t.year, t.month,
                                 t.day, t.hour, t.minute,
                                 t.second)

    file_name = "web_static_{}.tgz".format(time)

    local('tar -czvf versions/{} web_static'.format(file_name))

    file_path = "versions/{}".format(file_name)
    if path.exists(file_path):
        return file_path
    else:
        return None


def do_deploy(archive_path):
    """deploys the web_static
    """
    if isfile(archive_path):
        pre_path = archive_path.split("/")[1]
        put(archive_path, "/tmp/")
        tmp_path = "/tmp/" + pre_path
        releases_path = "/data/web_static/releases/" + pre_path.split(".")[0]
        sudo("mkdir -p {:s}".format(releases_path))
        sudo("tar -xzf {:s} -C {:s}".format(tmp_path, releases_path))
        sudo("rm {:s}".format(tmp_path))
        all_path_w = releases_path + "/web_static/*"
        dictory_path = releases_path + "/web_static/"
        sudo("mv {:s} {:s}".format(all_path_w, releases_path))
        sudo("rm -rf {:s}".format(dictory_path))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {:s} /data/web_static/current".format(releases_path))
        print("New version deployed!")
        return True
    else:
        return False