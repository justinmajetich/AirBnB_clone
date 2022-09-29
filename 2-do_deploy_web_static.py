#!/usr/bin/python3
"""
This script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy
Usage:
    fab -f 2-do_deploy_web_static.py do_deploy:
    archive_path=versions/<file_name> -i my_ssh_private_key

Example:
    fab -f 2-do_deploy_web_static.py do_deploy:
    archive_path=versions/web_static_20170315003959.tgz -i my_ssh_private_key
"""

from fabric.api import env, put, run
from os.path import exists
import shlex
env.hosts = ['3.236.55.133', '44.192.95.89']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """All remote commands must be executed on your both web servers
    (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)"""
    if not exists(archive_path):
        return False
    try:
        package_name = archive_path.replace('/', ' ')
        package_name = shlex.split(package_name)
        package_name = package_name[-1]

        updated_package = package_name.replace('.', ' ')
        updated_package = shlex.split(updated_package)
        updated_package = updated_package[0]

        releases_path = "/data/web_static/releases/{}/".format(updated_package)
        tmp_path = "/tmp/{}".format(package_name)

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(releases_path))
        run("tar -xzf {} -C {}".format(tmp_path, releases_path))
        run("rm {}".format(tmp_path))
        run("mv {}web_static/* {}".format(releases_path, releases_path))
        run("rm -rf {}web_static".format(releases_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(releases_path))
        print("New version deployed!")
        return True
    except BaseException:
        return False
