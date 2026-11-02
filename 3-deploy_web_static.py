#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from
the contents of the web_static folder
and uploads and deploy on servers"""
from fabric.api import *
from datetime import datetime


env.hosts = ['54.157.132.219', '100.26.156.236']


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    local('mkdir -p versions')
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    name = "web_static_{}.tgz".format(time)
    file_name = "versions/{}".format(name)
    local("tar -cvzf {} web_static/".format(file_name))
    if file_name:
        return (file_name)
    else:
        return None


def do_deploy(archive_path):
    """Deploy a .tgz archive from the contents
    of the web_static to the server"""
    if not archive_path:
        return False
    # Upload to /tmp/ in the server
    # put(archive_path, "/tmp/")
    with cd("/tmp/"):
        res = put(archive_path, "/tmp/")
        print(res)

    # Make directory for the file extraction
    run("mkdir -p /data/web_static/releases/")

    # GEt the file name
    file_name = archive_path.split("/")[-1]

    # Extract the file from archive
    remote_name = file_name.split(".")[0]
    run("mkdir -p /data/web_static/releases/{}".format(remote_name))
    run("tar -xzf /tmp/{} -C /data/web_static/releases/{}"
        .format(file_name, remote_name))

    # Delete the archive from the web serve
    run("rm /tmp/{}".format(file_name))

    # Move file out of web_static
    run("mv /data/web_static/releases/{}/web_static/* "
        "/data/web_static/releases/{}/".format(remote_name, remote_name))

    # Delete the symbolic link
    run("rm -rf /data/web_static/current")

    # Create a new the symbolic link
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
        .format(remote_name))
    return (True)


def deploy():
    """Execute the functions to create archive and deploy"""
    path = do_pack()
    if not path:
        return False
    ret = do_deploy(path)
    return (ret)
