#!/usr/bin/python3
"""the Fabric file"""

from fabric.api import local, env, put, run
from datetime import datetime
import os.path

env.hosts = ['34.227.228.210', '35.237.5.93']


def do_deploy(archive_path):
    """deploy an archive"""

    if not os.path.exists(archive_path):
        return False

    try:
        archiveName = archive_path[9:]
        archiveNameWithoutExtension = archiveName[:-4]
        newPathDir = "/data/web_static/releases/"

        put(archive_path, '/tmp/' + archiveName)
        run("mkdir -p " + newPathDir +
            archiveNameWithoutExtension)
        run("tar -xzvf /tmp/" + archiveName + " -C " +
            newPathDir + archiveNameWithoutExtension +
            " --strip-components=1")
        run("rm -f /tmp/" + archiveName)
        run("rm -f /data/web_static/current")
        run("sudo ln -sf " + newPathDir +
            archiveNameWithoutExtension +
            " /data/web_static/current")

        return True
    except:
        return False


def do_pack():
    """Pack up web_static"""

    try:
        currentTime = datetime.now()

        tarArchiveName = "web_static_" + \
                         currentTime.strftime("%Y%m%d%H%M%S") + ".tgz"
        tarArchivePath = "versions/" + tarArchiveName

        local("mkdir -p versions")

        local("tar -czvf " + tarArchivePath + " web_static")
        return tarArchivePath
    except:
        return None
