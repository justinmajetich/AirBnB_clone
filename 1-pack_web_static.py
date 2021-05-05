#!/usr/bin/python3
"""script that generates a .tgz archive from the contents of the web_static
 folder of your AirBnB Clone repo, using the function do_pack"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Compress before sending"""
    local("mkdir -p versions")
    # create the name of file in str format from datetime.now
    name = "web_static_" + datetime.strftime(datetime.now(),
                                             "%Y%m%d%H%M%S") + ".tgz"
    try:
        local("tar -czvf ./versions/{} ./web_static" .format(name))
        return(name)
    except:
        return(None)
