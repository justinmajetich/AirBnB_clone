#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""
from fabric.api import env, put, run
from os.path import exists

env.hosts = ["54.87.8.16", "34.229.206.87"]
env.user = "ubuntu"
env.key = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """Function to distribute an archive to your web servers"""
    if not exists(archive_path):
        return False
    try:


        file_name = archive_path.split("/")[-1]
        name = file_name.split(".")[0]
        path_name = "/data/web_static/releases/" + name
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(path_name))
        run('tar -xzf /tmp/{} -C {}/'.format(file_name, path_name))
        run("rm /tmp/{}".format(file_name))
        run("mv {}/web_static/* {}".format(path_name, path_name))
        run("rm -rf {}/web_static".format(path_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/ /data/web_static/current'.format(path_name))
                # Create 'hbnb_static' directory if it doesn't exist
        if not isdir("/var/www/html/hbnb_static"):
            run("sudo mkdir -p /var/www/html/hbnb_static")

        # Sync 'hbnb_static' with 'current'
        run("sudo cp -r /data/web_static/current/* /var/www/html/hbnb_static/")

        print("New version deployed!")
        return True
    except Exception:
        return False
