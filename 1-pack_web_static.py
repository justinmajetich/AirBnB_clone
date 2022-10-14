#!/usr/bin/python3
"""
    Script generates a .tgz archive from web_static folder
"""


def do_pack():
    """
    function creates a .tgz
    """
    from fabric.operations import local
    from datetime import datetime

    name = "./versions/web_static_{}.tgz"
    name = name.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    create = local("tar -cvzf {} web_static".format(name))
    if create.succeeded:
        return name
    else:
        return None

if __name__ == "__main__":
    do_pack()
