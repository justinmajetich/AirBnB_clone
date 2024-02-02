#!/usr/bin/python3
"""pack_web_static
Generate a .tgz archive from static web files
"""

import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """Generate a .tgz archive from the content of `web_static` folder"""

    if not os.path.exists("versions"):
        os.mkdir("versions")
    archive = (
        "versions/web_static_"
        f"{datetime.now().strftime('%Y%m%d%H%M%S')}.tgz")
    print(f"Packing web_static to {archive}")
    local(f"tar -cvzf {archive} web_static")

    if os.path.exists(archive):
        archive_size = os.path.getsize(archive)
        print(f"web_static packed: {archive} -> {archive_size} Bytes")
        return os.path.abspath(archive)
    else:
        return None
