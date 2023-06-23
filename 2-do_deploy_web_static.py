#!/usr/bin/python3
from fabric.api import env, put, run, local
from os.path import exists, isdir
import os.path
import re

env.user = 'ubuntu'
env.hosts = ['54.197.135.244', '54.167.3.103']
env.key_filename = '~/.ssh/id_rsa'

def do_deploy(archive):
    if not exists(archive):
        return False

    put(archive, "/tmp/")

    file = re.search(r'[^/]+$', archive).group(0)
    folder = "/data/web_static/releases/{}".format(
        os.path.splitext(file)[0])

    if not exists(folder):
        run("mkdir -p {}".format(folder))

    run("tar -xzf /tmp/{} -C {}".format(file, folder))

    run("rm /tmp/{}".format(file))

    run("mv {}/web_static/* {}".format(folder, folder))

    run("rm -rf {}/web_static".format(folder))

    run("rm -rf /data/web_static/current")

    run("ln -s {} /data/web_static/current".format(folder))

    if not isdir("/var/www/html/hbnb_static"):
        run("sudo mkdir -p /var/www/html/hbnb_static")

    run("sudo cp -r /data/web_static/current/* /var/www/html/hbnb_static/")

    print("New version deployed!")
    return True

# Usage:
# fab -f 2-do_deploy_web_static.py do_deploy:/path/to/file.tgz
