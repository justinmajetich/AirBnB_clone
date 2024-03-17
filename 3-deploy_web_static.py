#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers
"""

from fabric.api import env, local, put, run
from os.path import exists
from datetime import datetime

env.hosts = ['100.26.20.151', '54.82.197.5']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        (str): Archive path if successfully generated, None otherwise.
    """
    try:
        # Create the versions directory if it doesn't exist
        if not os.path.exists("versions"):
            local("mkdir -p versions")

        # Create the file name with current date and time
        current_time = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(current_time)

        # Create the .tgz archive
        local("tar -cvzf {} web_static".format(file_name))

        return file_name
    except Exception as e:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.

    Args:
        archive_path (str): Path to the archive to be deployed.

    Returns:
        (bool): True if all operations are successful, False otherwise.
    """
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        file_name = archive_path.split('/')[-1]
        folder_name = file_name.split('.')[0]
        path = "/data/web_static/releases/"
        run('mkdir -p {}{}/'.format(path, folder_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, folder_name))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, folder_name))
        run('rm -rf {}{}/web_static'.format(path, folder_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, folder_name))
        return True
    except Exception as e:
        return False


def deploy():
    """
    Calls do_pack() to generate archive and then do_deploy() to deploy it.
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
