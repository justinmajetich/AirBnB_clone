#!/usr/bin/python3
"""
    a Fabric script that generates a .tgz archive
    from the contents of the web_static folder of your
    AirBnB Clone repo, using the function do_pack
"""

from os.path import isdir
from fabric.api import local
from datetime import datetime as dt


def do_pack():
    """ Fabric script to generate a .tgz archive """
    try:
        # get current time and set it as follows:
        # <year><month><day><hour><minute><second>
        crTime = dt.now().strftime("%Y%m%d%H%M%S")

        # create folder 'versions' if it doesn’t exist
        if isdir('versions') is False:
            local('mkdir versions')

        # set archive name as follows:
        # web_static_<year><month><day><hour><minute><second>.tgz
        archName = f'versions/web_static_{crTime}.tgz'

        # create an archive of the directory 'web_static'
        local(f'tar -cfvz {archName} web_static')

        # return the archive path
        return archName

    except Exception:
        return None
