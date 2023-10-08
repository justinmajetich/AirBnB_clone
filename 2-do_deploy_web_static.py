#!/usr/bin/python3
# fabric script that creat an archeive of the web_static dir

from datetime import datetime
from fabric.api import *
import os


env.hosts = ['34.224.16.178', '54.174.245.13']
env.key_filename = '~/.ssh/school'
env.user = 'ubuntu'

def do_pack():
    """
    archieving web_static dir
    """
#   create  versions directory if not exits
    local("mkdir -p versions")

    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"web_static_{date}.tgz"
    result = local(f"tar -czvf {file_name} web_static ")
    local(f"mv {file_name} ./versions")
#   checking if success

    if result.succeeded:
        return f"versions/{file_name}"
    else:
        return None

def do_deploy(archieve_path):
    """
    upload the web_static achieve to the servers
    """
    if not os.path.exists(archive_path):
        return False
    archive_name = archive_path.split('/')[-1]
    folder_name = archive_name[:-4]
    try:
        put(local_path=archive_path, remote_path="/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(folder_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            archive_name, folder_name))
        run("rm /tmp/{}".format(archive_name))
        run("mv /data/web_static/releases/{}/web_static/*\
 /data/web_static/releases/{}/".format(folder_name, folder_name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(
            folder_name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}\
        /data/web_static/current".format(folder_name))
    except Exception:
        return False
    else:
        print("New version deployed!")
        return True

