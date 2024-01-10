#!/usr/bin/python3

from datetime import datetime
from fabric.api import local
from os.path import exists


def do_pack():
    """
    Generates a .tgz archive web_static.

    Returns:
        str: The path to the generated archive
        file, or None if an error occurs.
    """
    dt = datetime.now().strftime("%Y%m%d%H%M%S")
    conf = f"versions/web_static_{dt}.tgz"
    cmd = f"tar -cvzf {conf} web_static"
    try:
        if not exists("versions"):
            local("mkdir versions")
        local(cmd)
        return conf
    except Exception:
        return None