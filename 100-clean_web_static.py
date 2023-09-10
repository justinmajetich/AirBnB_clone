#!/usr/bin/python3
"""
    a Fabric script (based on the file 3-deploy_web_static.py)
    that deletes out-of-date archives, using the function do_clean:
"""

from fabric.api import *

env.hosts = ['34.203.33.172', '54.210.234.151']
env.user = 'ubuntu'


def do_clean(number=0):
    """ deletes out-of-date archives """

    number = int(number)
