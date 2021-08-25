#!/usr/bin/python3


from fabric.api import local, put, run, env
import time
import os

env.hosts = ['34.138.56.48', '34.74.249.41']


def do_pack():
    """
        generates a .tgz archive from the contents of the web_static folder
    """
    try:
        now = time.strftime("%Y%m%d%H%M%S")
        name = "web_static_{:s}.tgz".format(now)
        path = "versions/{:s}".format(name)
        dest_path = "{:s}/".format("web_static")

        local("mkdir -p versions")
        local("tar -cvzf {:s} {}".format(path, dest_path))

        return path
    except Exception:
        return None


def do_deploy(archive_path):
    """
        distributes an archive to your web servers
    """
    if None is archive_path or not os.path.exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        file_name = archive_name.split(".")[0]
        dest_path = "/tmp/{}".format(archive_name)
        release_path = "/data/web_static/releases/{}/".format(file_name)

        put(archive_path, dest_path)
        run("mkdir -p {}".format(release_path))
        run("tar -xzf {} -C {}".format(dest_path, release_path))
        run("rm {}".format(dest_path))
        run("mv {}web_static/* {}".format(release_path, release_path))
        run("rm -rf {}web_static".format(release_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_path))
        print("New version deployed!")

        return True
    except Exception:
        return False


def deploy():
    """
        creates and distributes an archive to your web servers
    """
    archive_path = do_pack()

    if False is archive_path:
        return False

    return do_deploy(archive_path)
