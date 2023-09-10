#!/usr/bin/python3
"""
    a Fabric script (based on the file 1-pack_web_static.py)
    that distributes an archive to your web servers, using
    the function do_deploy:
"""

from os.path import exists
from fabric.api import local, put, run, env

env.hosts = ['34.203.33.172', '54.210.234.151']


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
