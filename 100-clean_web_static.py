#!/usr/bin/python3
"""web server distribution"""
from fabric.api import *
from fabric.state import commands, connections
import os.path

env.user = 'ubuntu'
env.hosts = ["104.196.155.240", "34.74.146.120"]
env.key_filename = "~/id_rsa"


def do_clean(number=0):
    """deletes out-of-date archives"""
    local('ls -t ~/AirBnB_Clone_V2/versions/').split()
    with cd("/data/web_static/releases"):
        target_R = sudo("ls -t .").split()
    paths = "/data/web_static/releases"
    number = int(number)
    if number == 0:
        num = 1
    else:
        num = number
    if len(target_R) > 0:
        if len(target) == number or len(target) == 0:
            pass
        else:
            cl = target[num:]
            for i in range(len(cl)):
                local('rm -f ~/AirBnB_Clone_V2/versions/{}'.format(target[-1]))
        rem = target_R[num:]
        for j in range(len(rem)):
            sudo('rm -rf {}/{}'.format(paths, rem[-1].strip(".tgz")))
    else:
        pass
