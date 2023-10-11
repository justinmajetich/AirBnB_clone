#!/usr/bin/python3
"""
    a Fabric script that generates a .tgz archive
    from the contents of the web_static folder of your
    AirBnB Clone repo, using the function do_pack
"""

from fabric.api import *
from os.path import isdir, exists
from datetime import datetime as dt

env.hosts = ['34.203.33.172', '54.210.234.151']


def do_pack():
    """ Fabric script to generate a .tgz archive """
    try:
        # get current time and set it as follows:
        # <year><month><day><hour><minute><second>
        crTime = dt.now().strftime("%Y%m%d%H%M%S")

        # create folder 'versions' if it doesn’t exist
        if isdir('versions') is not True:
            local('mkdir -p versions')

        # set archive name as follows:
        # web_static_<year><month><day><hour><minute><second>.tgz
        archName = f'versions/web_static_{crTime}.tgz'

        # create an archive of the directory 'web_static'
        local(f'tar -czvf {archName} web_static')

        # return the archive path
        return archName

    except Exception:
        return None


def do_deploy(archive_path):
    """ a function that distributes an archive to web servers """

    if exists(archive_path) is False:
        return False

    try:
        # get archive file name, name and the path to decompress archive
        archName = archive_path.split('/')[-1]
        Fpath = f"/data/web_static/releases/{archName.split('.')[0]}"

        # save the archive to '/tmp/'
        put(archive_path, '/tmp/')

        # create the decompression file
        run(f'mkdir -p {Fpath}/')

        # decompress archive to created file
        run(f'tar -xzf /tmp/{archName} -C {Fpath}/')

        # delete the archive from the web server
        run(f'rm /tmp/{archName}')

        # move the files back
        # linked to the new version of your code;
        # (/data/web_static/releases/<archive filename without extension>)
        run(f'mv {Fpath}/web_static/* {Fpath}/')
        run(f'rm -rf {Fpath}/web_static')

        # delete the symbolic link /data/web_static/current
        # create a new the symbolic link /data/web_static/current
        run(f'rm -rf /data/web_static/current')
        run(f'ln -s {Fpath}/ /data/web_static/current')

        return True
    except Exception:
        return False


def deploy():
    """ creates and distributes an archive to your web servers """

    archive = do_pack()
    if (archive is None):
        return False

    value = do_deploy(archive)
    return value
