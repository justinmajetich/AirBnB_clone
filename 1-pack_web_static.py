#!/usr/bin/python3
"""
Compress the files in web_static to create
an archive, for deployment
Usage: ./1-pack_web_static.py do_pack
"""

from fabric.api import local
from datetime import datetime


def do_pack() -> None:
    """
    Pack the files to an archive for deployment
    Args:
        None
    Returns:
        Path(path of the archive) - if true
        None ( if any exceptions occur)
    """
    c_time = datetime.now()
    arch_name = "web_static_{}.tgz".format(c_time.strftime("%Y%m%d%H%M%S"))
    local('mkdir -p versions/')
    create = local('tar -cvzf versions/{} web_static'.format(arch_name))
    if create is not None:
        return arch_name
    else:
        return None
