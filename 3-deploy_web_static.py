#!/usr/bin/python3
"""
Fabric script creates and distribute an archive to your web servers.
Prototype function: def deploy():
The script should:
        Call the do_pack() function and store the path of the created archive
        Return False if no archive has been created
        Call do_deploy(archive_path) function, using new path of new archive
        Return the return value of do_deploy
All remote commands must be executed on both servers using env.hosts variable
You must use this script to deploy it on your servers.
"""
from fabric.api import local, env, run, put
from datetime import datetime
import os


env.hosts = ['<34.234.193.7>', '<54.174.67.136>']
env.user = 'ubuntu'


def do_pack():
    """Creates a tar archive of web_static directory"""
    try:
        if not os.path.exists("versions"):
            os.mkdir("versions")
        date_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(date_time)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception:
        return None


def do_deploy(archive_path):
    """Distributes archive to web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        filename = os.path.basename(archive_path)
        path = "/data/web_static/releases/{}/".format(filename[:-4])
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path))
        run("tar -xzf /tmp/{} -C {}".format(filename, path))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(path, path))
        run("rm -rf {}web_static".format(path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path))
        return True
    except Exception:
        return False


def deploy():
    """Create and distribute archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
