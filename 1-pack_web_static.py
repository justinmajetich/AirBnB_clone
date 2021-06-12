#!/usr/bin/python3
"""the Fabric file"""

from fabric.api import local
from datetime import datetime

def do_pack():
    """Fabric script that generates a .tgz archive from the contents of the web_static folder"""

    now = datetime.now()

    tarArchiveName = "web_static_" + now.strftime("%Y%m%d%HM%S") + ".tgz"
    tarArchivePath = "versions/" + tarArchiveName

    local("mkdir -p versions")

    local("tar -czvf " + tarArchivePath + " web_static")
