#!/usr/bin/python3
"""the Fabric file"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """create a .tgz archive from the contents of web_static folder"""

    currentTime = datetime.now()

    tarArchiveName = "web_static_" + \
                     currentTime.strftime("%Y%m%d%HM%S") + ".tgz"
    tarArchivePath = "versions/" + tarArchiveName

    local("mkdir -p versions")

    local("tar -czvf " + tarArchivePath + " web_static")
