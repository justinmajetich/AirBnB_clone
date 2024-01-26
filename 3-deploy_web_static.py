#!/usr/bin/python3
"""Fab file for task 3 Deploy"""
from fabric.api import put, env, sudo
import os

env.warn_only = True


def deploy():
    """
    Fully creates and distributes an archive to web servers
    Return:
        False if archive_path doesnt exist
    """
    do_deploy = __import__('2-do_deploy_web_static').do_deploy
    do_pack = __import__('1-pack_web_static').do_pack
    do_deploy()
