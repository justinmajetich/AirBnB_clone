#!/usr/bin/python3
from fabric.api import run, local, put, env
import datetime
import os


def do_pack():
    """do pack method"""
    time = datetime.datetime.now()
    date = (str(time.year) + str(time.month) + str(time.day) + str(time.hour) +
            str(time.minute) + str(time.second))
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz ./web_static".format(date))
        return "./versions/web_static_{}.tgz".format(date)
    except:
        return None


env.hosts = ['35.229.42.147', '54.90.157.131']


def do_deploy(archive_path):
    """
     Fabric script 
     (based on the file 1-pack_web_static.py) 
     that distributes an archive to your web servers, 
     using the function do_deploy

    """
    if os.path.exists(archive_path) is False:
        return False
    try:
        upload = put(archive_path, "/tmp/")
        name = archive_path[9:-4]
        rmt_path = "/data/web_static/releases/" + name
        run("mkdir {}".format(rmt_path))
        run("tar -xvzf /tmp/{}.tgz --directory {}/".format(name, rmt_path))
        run("rm /tmp/{}.tgz".format(name))
        run("rm /data/web_static/current")
        run("ln -nsf /data/web_static/releases/{} /data/web_static/current"
            .format(name))
        run("mv {}/web_static/* {}".format(rmt_path, rmt_path))
        run("rm -d {}/web_static/".format(rmt_path))
        return True
    except:
        return False 
    