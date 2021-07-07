#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents
# of the web_static folder of your AirBnB Colne repo,
# using the function do_pack
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    that fenerates a .tgz archive from the contents of the web_static folder
    """
    dt = datetime.now()
    file = 'web_static' + str(dt.year) + str(dt.month) + str(dt.day)
    file = file + str(dt.hour) + str(dt.minute) + str(dt.second) + '.tgz'
    local('mkdir -p versions')
    directory = local('tar -cvzf versions/{} web_static'. format(file))
    if directory.failed:
        return None
    return 'versions/{}'.format(file)
