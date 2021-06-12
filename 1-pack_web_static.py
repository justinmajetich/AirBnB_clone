#!/usr/bin/python3
"""the Fabric file"""

from fabric.api import local
from datetime import datetime


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
