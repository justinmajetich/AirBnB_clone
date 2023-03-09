#!/usr/bin/python3
"""deploy files"""
from os.path import exists
do_pack = __import__('1-pack_web_static')
do_deploy =  __import__('2-do_deploy_web_static')



def deploy():
    """deploy files"""
    archive = do_pack()
    if not exists(archive):
        return False
    return do_deploy(archive)
