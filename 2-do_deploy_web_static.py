#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""
from fabric.api import run, put, env
from os.path import exists

env.hosts = ['34.75.252.164', '35.237.149.147']


def do_deploy(archive_path):
    """ Fabric script that distributes an archive to your web servers"""
    if exists(archive_path) is True:
        try:
            filename = archive_path.split('/')[-1]
            no_ex = filename.split('.')[0]
            put(archive_path, '/tmp/')
            foldername = "/data/web_static/releases/" + no_ex
            run("mkdir -p {}/".format(foldername))
            run("tar -xzf /tmp/{} -C {}/".format(filename, foldername))
            run("rm  /tmp/{}".format(filename))
            run('mv {}/web_static/* {}/'.format(foldername, foldername))
            run("rm -rf {}/web_static".format(foldername))
            run("rm -rf /data/web_static/current")
            run("ln -s {}/\
                /data/web_static/current".format(foldername))
            return True
        except:
            return False
    return False
