#!/usr/bin/python3
'''Fabric script to generate .tgz archive'''
from datetime import datetime
from fabric.api import local
from fabric.decorators import runs_once


@runs_once
def do_pack():
    '''generates .tgz archive from the contents of the web_static folder'''
    path = f'versions/web_static_{datetime.now():%Y%m%d%H%M%S}.tgz'
    result = local(f'tar -cvzf {path} web_static')

    return path if result.succeeded else None

