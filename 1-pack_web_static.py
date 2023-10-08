#!/usr/bin/python3
""" This is Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """This is a function that will generate the .tgz archive contents
        using the datetime to show when the .tgz is generated.
    """
    year = datetime.utcnow().year
    month = datetime.utcnow().month
    day = datetime.utcnow().day
    hour = datetime.utcnow().hour
    minute = datetime.utcnow().minute
    second = datetime.utcnow().second

    # now = datetime.now()
    # timestamp = now.strftime("%Y%m%d%H%M%S")

    # To create version directory
    local('mkdir -p versions')

    content = f"versions/web_static_{year}{month}{day}{hour}{minute}{second}.tgz"
    # content = f"versions/web_static_{timestamp}"
    # To generate the .tzg content
    result = local(f'tar -czvf {content} web_static/')
    if result.succeeded:
        return content
    else:
        return None
