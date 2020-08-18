#!/usr/bin/python3

"""
script that distributes an archive to your web servers
using the function do_deploy
"""

from fabric.api import *
from os.path import isfile
from os import path
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

"""
def do_deploy(archive_path):
    #
    #     script that distributes an archive to your web servers
    #     using the function do_deploy

    if path.isfile(archive_path):
        # Upload the archive to the /tmp/ directory of the web server
        local_path = archive_path
        remote_path = "/tmp/"

        put(archive_path, remote_path)

        path_to_uncompress = "/data/web_static/releases/"
        file_name = archive_path.split('/')[1]
        filename_noextension = file_name.split('.')[0]

        # Creating folder /data/web_static/releases/web_static_202081720267
        sudo("mkdir -p {}{}/".format(path_to_uncompress, filename_noextension))

        # Uncompress the archive to the folder "/data/web_static/releases/"
        sudo("tar -xzf {}{} -C {}{}/".format(remote_path, file_name,
                                             path_to_uncompress,
                                             filename_noextension))

        # Delete the archive from the web server
        sudo('rm {}{}'.format(remote_path, file_name))
        # move files
        sudo("mv {}{}/web_static/* {}{}/.".format(path_to_uncompress,
                                                  filename_noextension,
                                                  path_to_uncompress,
                                                  filename_noextension))
        # Delete the symbolic link /data/web_static/current from the web server
        sudo("rm -rf {}{}/web_static/".format(path_to_uncompress,
                                              filename_noextension))
        sudo('rm -rf /data/web_static/current')
        # Create a new the symbolic link on the web server
        # linked to the new version of your code
        sudo("ln -s {}{}/ /data/web_static/current".format(
            remote_path, filename_noextension))

        print("New version deployed!")
        return True
    else:
        return False
"""


def do_deploy(archive_path):
    """deploys the
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


def deploy():
    """full deploy
    """
    filepath = do_pack()
    if filepath is None:
        return False
    else:
        return do_deploy(filepath)
