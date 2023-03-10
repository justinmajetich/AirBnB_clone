#!/usr/bin/python3
from fabric.api import local, run, put, env
from os.path import exists
env.hosts = ['<IP web-01>', '<IP web-02>']


def do_pack():
    """Creates a compressed archive of the web_static folder"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_file = "versions/web_static_{}.tgz".format(timestamp)
    local("mkdir -p versions")
    local("tar -czvf {} web_static".format(archive_file))
    if exists(archive_file):
        return archive_file
    return None


def do_deploy(archive_path):
    """Distributes an archive to a web server"""
    if not exists(archive_path):
        return False

    archive_name = archive_path.split("/")[-1]
    folder_name = "/data/web_static/releases/{}"\
        .format(archive_name.split(".")[0])
    put(archive_path, "/tmp/")
    run("mkdir -p {}".format(folder_name))
    run("tar -xzf /tmp/{} -C {}".format(archive_name, folder_name))
    run("rm /tmp/{}".format(archive_name))
    run("mv {}/web_static/* {}".format(folder_name, folder_name))
    run("rm -rf {}/web_static".format(folder_name))
    run("rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(folder_name))
    return True


def deploy():
    """Creates and distributes an archive to two web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
