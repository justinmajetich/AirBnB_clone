#!/usr/bin/python3
"""
    Generate a .tgz archive from the contents of the web_static folder
    Deploy it to the web servers
"""

from os.path import isfile
from fabric.api import local, run, env, put
import time
env.hosts = ['35.196.21.97', '34.139.18.218']


def do_pack():
    """
        Generates a .tgz
        Return: archive path
    """
    time_now = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time_now))
        return ("versions/web_static_{}.tgz".format(time_now))
    except:
        return None


def do_deploy(archive_path):
    """
    Puts the archive in the web server
    Destination: /tmp/
    Uncompressed in:
        /data/web_static/releases/<archive filename without extension>
    Archive is deleted from webserver after
    Symbolic link is recreated to point to the folder mentioned above
    Returns: True id all ops are done correctly
    """
    if (isfile(archive_path) is False):
        return False
    try:
        localp = archive_path.split("/")[-1]
        new_folder = ("/data/web_static/releases/" + localp.split(".")[0])
        put(archive_path, "/tmp")
        run("mkdir {}".format(new_folder))
        run("tar -xzf /tmp/{} -C {}".format(localp, new_folder))
        run("rm /tmp/{}".format(localp))
        run("mv {}/web_static/* {}/".format(new_folder, new_folder))
        run("rm -rf {}/web_static".format(new_folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(new_folder))
        return True
    except:
        return False


def deploy():
    """
    Calls do_pack() function then do_deploy
    """
    archive_path = do_pack()
    if archive_path:
        return do_deploy(archive_path)
