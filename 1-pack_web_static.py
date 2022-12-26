#!/usr/bin/python3
"""
compress before sending
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
	"""generates an archive"""
	myVar = vars()
    now = datetime.now().strftime("%Y%M%D%H%M%S")
    local(mkdir -p /versions/)
	local(tar -czvf "web_static_{}.tgz".format(now) /versions)
    if os.path.exists("/versions/web_static_{}.tgz".format(now)):
        return os.path.normpath("/versions/web_static_{}.tgz".format(now))
    else:
        return None
