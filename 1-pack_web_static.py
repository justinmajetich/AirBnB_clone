#!/usr/bin/python3
""" Fabric script that generates a .tgz archive 
from the contents of the web_static """


def do_pack():
    """ for generate .tgz """
    from fabric.api import local
    import time

    local("mkdir -p versions")
    created = (time.strftime("%Y%m%d%H%M%S"))
    compressed = local("tar -cvzf versions/web_static_{}.tgz web_static"
                       .format(created))
    if not compressed.succeeded:
        return "versions/web_static_{}.tgz".format(created)
    else:
        return None
