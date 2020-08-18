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
    noext = archive_path.replace(".tgz", "").split("/")[1]
    if not path.exists(archive_path):
        return False

    try:
        put('{}'.format(archive_path), '/tmp/')
        archive_path = archive_path.split("/")[1]

        server_dir = "/data/web_static/releases/{}".format(noext)
        run('mkdir -p {}'.format(server_dir))

        run(' tar -xzf /tmp/{} -C {}'.format(archive_path, server_dir))
        run('rm /tmp/{}'.format(archive_path))
        run('mv {}/web_static/* {}/'.format(server_dir, server_dir))
        run('rm -rf {}/web_static'.format(server_dir))
        run('unlink /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(server_dir))
    except Exception:
        return False
    return True
