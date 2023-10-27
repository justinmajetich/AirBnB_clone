#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack."""

from fabric.api import env

env.hosts = ['54.236.217.62', '100.26.229.89']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    '''Function that generates a .tgz archive from the contents of the
    web_static folder.'''
    from fabric.api import local
    from datetime import datetime
    print("Packing web_static to versions/web_static_20170314233357.tgz")
    local('mkdir -p versions')
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file = f"versions/web_static_{date}.tgz"
    try:
        local(f'tar -cvzf {file} web_static')
        return file
    except Exception:
        return None


def do_deploy(archive_path):
    '''Function that distributes an archive to your web servers,
    using the function do_deploy.'''
    from fabric.api import put, run
    from os.path import exists

    if exists(archive_path) is False:
        return False

    try:
        put(archive_path, "/tmp/")
        file = archive_path.split('/')[-1]
        folder = f"/data/web_static/releases/{file.split('.')[0]}"
        run("sudo mkdir -p {}".format(folder))
        run("sudo tar -xzf /tmp/{} -C {}".format(file, folder))
        run("sudo rm /tmp/{}".format(file))
        run("sudo mv {}/web_static/* {}/".format(folder, folder))
        run("sudo rm -fr {}/web_static".format(folder))
        run("sudo rm -fr /data/web_static/current")
        run("sudo ln -s {}/ /data/web_static/current".format(folder))
        return True
    except Exception:
        return False
