#!/usr/bin/python3
"""
    Distributes an archive to your web servers,
    using the function do_deploy
    def do_deploy(archive_path):
    Return False iff archive path doesn't exist
"""

from fabric.api import put, run, env, sudo
from os.path import exists
env.hosts = ['52.91.122.203', '34.224.17.18']
env.user = 'ubuntu'
env.identity = '~/.ssh/school'
env.password = None

run("rm -rf /data/web_static/releases/web_static_20230506221613/images")
run("rm -rf /data/web_static/releases/web_static_20230506221613/styles")

def do_deploy(archive_path):
    """
    Deploys an archive to a server
    """
    if exists(archive_path) is False:
        return False
    try:
        archive_name = archive_path.split("/")[-1]
        no_ext = archive_name.split(".")[0]
        path_no_ext = "/data/web_static/releases/" + no_ext

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_no_ext))
        run("tar -xzf /tmp/{} -C {}/".format(archive_name, path_no_ext))
        run("rm /tmp/{}".format(archive_name))
        run("mv {}/web_static/* {}/".format(path_no_ext, path_no_ext))
        run("rm -rf {}/web_static".format(path_no_ext))
        run("rm -rf /data/web_static/current")
        sudo("ln -s {}/ /data/web_static/current".format(path_no_ext))
        sudo("chmod -R 755 {}".format(path_no_ext))

        print("New version deployed!")
        return True
    except FileNotFoundError:
        return False
