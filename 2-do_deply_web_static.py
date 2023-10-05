#!/usr/bin/python3
"""
Fabric scripts that distribute an archive to web servers
"""
import os
from fabric.api import run, env, put

env.hosts = ['52.3.245.154', '54.157.143.250']


def do_deploy(archive_path):
    """ deploying archive function """
    if not os.path.exists(archive_path):
        return False

    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    # Upload the archive to /tmp
    if put(archive_path, "/tmp/{}".format(file)).failed:
        return False

    # Remove existing release directory
    if run("rm -rf /data/web_static/releases/{}/".format(name)).failed:
        return False

    # Create a new release directory
    if run("mkdir -p /data/web_static/releases/{}/".format(name)).failed:
        return False

    # Extract the contents of the archive to the new release directory
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file, name)).failed:
        return False

    # Remove the uploaded archive
    if run("rm /tmp/{}".format(file)).failed:
        return False

    # Move contents to the proper location
    if run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".
           format(name, name)).failed:
        return False

    # Remove the old web_static directory
    if run("rm -rf /data/web_static/releases/{}/web_static".format(name)).failed:
        return False

    # Remove the current symbolic link
    if run("rm -rf /data/web_static/current").failed:
        return False

    # Create a symbolic link to the new release
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed:
        return False

    return True
