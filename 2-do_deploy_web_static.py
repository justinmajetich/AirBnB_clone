#!/usr/bin/python3
"""
Deploy archive!
"""
from fabric.api import run, env, put
from os import path

env.hosts = ["34.231.110.206", "3.239.57.196"]

def do_deploy(archive_path):
    """
    Fabric script (based on the file 1-pack_web_static.py) that distributes an
    archive to your web servers, using the function do_deploy
    """
    if not path.exists(archive_path):
        return False

    archieve = archive_path.split("/")[-1]
    files = archieve.split(".")[0]
    file_loading = f"/tmp/{archieve}"

    if put(archive_path, file_loading).failed or \
        run(f"rm -rf /data/web_static/releases/{files}").failed or \
        run(f"mkdir -p /data/web_static/releases/{files}").failed or \
        run(f"tar -xzf /tmp/{archieve} -C /data/web_static/releases/{files}").failed or \
        run(f"rm -f /tmp/{archieve}").failed or \
        run("rm -rf /data/web_static/current").failed or \
        run(f"ln -s /data/web_static/releases/{files} /data/web_static/current").failed:
        return False

    return True
