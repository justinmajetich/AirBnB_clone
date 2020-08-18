#!/usr/bin/python3

"""
script that distributes an archive to your web servers
using the function do_deploy
"""

from fabric.api import *
from os import path
from datetime import datetime

env.hosts = ['34.73.51.195', '34.73.59.80']


def do_deploy(archive_path):
    """
        script that distributes an archive to your web servers
        using the function do_deploy
    """
    if path.exists(archive_path):
        # Upload the archive to the /tmp/ directory of the web server
        local_path = archive_path
        remote_path = "/tmp/"
        put(archive_path, remote_path)

        path_to_uncompress = "/data/web_static/releases/"
        file_name = archive_path.split('/')[1]
        filename_noextension = file_name.split('.')[0]

        # Creating folder /data/web_static/releases/web_static_202081720267
        sudo("mkdir -p {}{}".format(path_to_uncompress, filename_noextension))

        # Uncompress the archive to the folder "/data/web_static/releases/"
        sudo("tar -xzf {}{} -C {}{}".format(remote_path, file_name,
                                            path_to_uncompress,
                                            filename_noextension))

        # Delete the archive from the web server
        sudo('rm -f {}{}'.format(remote_path, file_name))
        # Delete the symbolic link /data/web_static/current from the web server
        sudo('rm -f /data/web_static/current')
        # Create a new the symbolic link on the web server
        # linked to the new version of your code
        sudo("ln -s {}{} /data/web_static/current".format(remote_path,
                                                          file_name))
        print("New version deployed!")
        return True
    else:
        return False
