#!/usr/bin/python3
"""the Fabric file"""

from fabric.api import local, env, put, run
from datetime import datetime
import os.path

env.hosts = ['34.227.228.210', '3.80.186.246']

def do_deploy(archive_path):
    """deploy an archive"""

    if not os.path.exists(archive_path):
        return False

    try:
        archiveName = archive_path[9:]
        archiveNameWithoutExtension = archiveName[:-4]

        put(archive_path, '/tmp/' + archiveName)
        run("mkdir -p /data/web_static/releases/" + archiveNameWithoutExtension)
        run("tar -xzvf /tmp/" + archiveName + " -C" + "/data/web_static/releases" + archiveNameWithoutExtension + " --strip-components=1")
        run("rm -f /tmp/" + archiveName)
        run("rm -f /data/web_static/current")
        run("ln -sf /data/web_static/releases/" + archiveNameWithoutExtension + " /data/web_static/current/")

        return True
    except:
        return False

def do_pack():
    """Pack up web_static"""

    now = datetime.now()

    tarArchiveName = "web_static_" + now.strftime("%Y%m%d%HM%S") + ".tgz"
    tarArchivePath = "versions/" + tarArchiveName

    local("mkdir -p versions")

    local("tar -czvf " + tarArchivePath + " web_static")
