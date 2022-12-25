#!/usr/bin/python3
"""creates and distributes an archive to
your web servers, using the function deploy"""
from fabric.api import env, local, put, run
from datetime import datetime
from os import path

env.hosts = ['35.175.132.172', '52.91.116.127']
env.user = 'ubuntu'


def deploy():
    """ Deploys """
    try:
        archive_path = do_pack()
        if archive_path is None or not path.exists(archive_path):
            raise Exception
        file_name_tgz = archive_path.split('/')[-1]
        file_name = file_name_tgz.split('.')[0]
        versions_path = "versions/{}".format(file_name_tgz)
        tmp_path = "/tmp/{}".format(file_name_tgz)
        release_path = "/data/web_static/releases/{}/".format(file_name)

        put(archive_path, '/tmp/')
        run("mkdir -p {}".format(release_path))
        run("tar -xzf {} -C {}".format(tmp_path, release_path))
        run("rm {}".format(tmp_path))
        run("mv {}web_static/* {}".format(release_path, release_path))
        run("rm -rf {}web_static".format(release_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_path))
        print("New version deployed!")
        return True
    except Exception:
        return False


def do_pack():
    """Prototype: def do_pack():"""
    try:
        if not path.exists("versions"):
            local('mkdir versions')
        created_time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_path = "versions/web_static_{}.tgz".format(created_time)
        local("tar -cvzf {} web_static".format(file_path))
        return file_path
    except Exception:
        return None
