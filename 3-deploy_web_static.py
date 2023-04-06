#!/usr/bin/python3
"""
Fabric script methods:
    do_pack: packs web_static/ files into .tgz archive
    do_deploy: deploys archive to webservers
    deploy: do_packs && do_deploys
Usage:
    fab -f 3-deploy_web_static.py deploy -i my_ssh_private_key -u ubuntu
"""
from fabric.api import local, env, put, run
from time import strftime
import os.path

env.hosts = ['3.229.122.175', '35.171.146.79']


def do_deploy(archive_path):
    """ deploy to a web server """
    if not os.path.exists(archive_path):
        return False
    try:
        file = archive_path.split("/")[-1]
        name = file.split(".")[0]
        path = "/data/web_static/releases/".format(name)
        put(archive_path, "/tmp/")
        run('sudo mkdir -p {}{}/'.format(path, name))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(file, path, name))
        run('sudo rm /tmp/{}'.format(file))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(path, name))
        run("sudo rm -rf {}{}/web_static".format(path, name))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {}{}/ /data/web_static/current".format(path, name))
        run('echo "New version deployed!"')
        return True
    except BaseException:
        # run('echo "wahala!"')
        return False


def deploy():
    """
        Creates and distributes an archive to your web servers
    """

    archive_path = do_pack()
    if os.path.exists(archive_path) is False:
        return False
    return do_deploy(archive_path)


def do_pack():
    """generate .tgz archive of web_static/ folder"""
    timenow = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(timenow)
        local("tar -cvzf {} web_static/".format(filename))
        return filename
    except:
        return None
