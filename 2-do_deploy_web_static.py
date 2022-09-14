#!/usr/bin/python3
"""This script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy"""


from fabric.api import env, put, run
from os.path import exists
import shlex
env.hosts = ['35.185.108.180', '34.229.169.234']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """All remote commands must be executed on your both web servers
    (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)"""
    if not exists(archive_path):
        return False
    try:
        pname = archive_path.replace('/', ' ')
        pname = shlex.split(pname)
        pname = pname[-1]

        wname = pname.replace('.', ' ')
        wname = shlex.split(wname)
        wname = wname[0]

        releases_path = "/data/web_static/releases/{}/".format(wname)
        tmp_path = "/tmp/{}".format(pname)

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
