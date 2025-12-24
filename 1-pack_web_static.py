#!/usr/bin/python3
"""
- This script generates a .tgz archive from the contents of the web_static
  folder of your AirBnB Clone repo, using the function `do_pack()`
- All archives must be stored in the folder versions
  If version folder doesn't exist, the function should create
- The function `do_pack` must return the archive path if the archive has been
correctly generated. Otherwise, it should return `None`
"""
from os.path import isdir
from datetime import datetime
from fabric import task


def do_pack():
    """Compress the web_static files to
       web_static_<year><month><day><hour><minute><second>.tgz archive
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    if not isdir("versions"):
        local("mkdir -p versions")

    archive_name = f"versions/web_static_{timestamp}.tgz"
    local("tar -cvzf {} web_static".format(archive_name))

    if not archive_name:
        return None

    return archive_name
