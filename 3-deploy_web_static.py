#!/usr/bin/python3
"""Tar, transfer, and deploy static html to webservers"""

from fabric import api, decorators
from fabric.contrib import files
from datetime import datetime
import os

api.env.hosts = ['holberton1', 'holberton3']
api.env.hosts = ['142.44.167.235', '144.217.246.199']
api.env.user = 'ubuntu'
api.env.key_filename = '~/.ssh/holberton'


def deploy():
    """Wrapper function to pack html files into tarball and transfer
    to web servers."""
    return do_deploy(do_pack())


@decorators.runs_once
def do_pack():
    """Function to create tarball of webstatic files from the web_static
    folder in Airbnb_v2.

    Returns: path of .tgz file on success, False otherwise
    """
    with api.settings(warn_only=True):
        isdir = os.path.isdir('versions')
        if not isdir:
            mkdir = api.local('mkdir versions')
            if mkdir.failed:
                return False
        suffix = datetime.now().strftime('%Y%m%d%M%S')
        path = 'versions/web_static_{}.tgz'.format(suffix)
        tar = api.local('tar -cvzf {} web_static'.format(path))
        if tar.failed:
            return False
        size = os.stat(path).st_size
        print('web_static packed: {} -> {}Bytes'.format(path, size))
        return path


def do_deploy(archive_path):
    """Function to transfer `archive_path` to web servers.

    Args:
        archive_path (str): path of the .tgz file to transfer

    Returns: True on success, False otherwise.
    """
    if not os.path.isfile(archive_path):
        return False
    with api.cd('/tmp'):
        basename = os.path.basename(archive_path)
        root, ext = os.path.splitext(basename)
        outpath = '/data/web_static/releases/{}'.format(root)
        try:
            putpath = api.put(archive_path)
            if files.exists(outpath):
                api.run('rm -rdf {}'.format(outpath))
            api.run('mkdir -p {}'.format(outpath))
            api.run('tar -xzf {} -C {}'.format(putpath[0], outpath))
            api.run('rm -f {}'.format(putpath[0]))
            api.run('mv -u {}/web_static/* {}'.format(outpath, outpath))
            api.run('rm -rf {}/web_static'.format(outpath))
            api.run('rm -rf /data/web_static/current')
            api.run('ln -s {} /data/web_static/current'.format(outpath))
            print('New version deployed!')
        except:
            return False
        else:
            return True
