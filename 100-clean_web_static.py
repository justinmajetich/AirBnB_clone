#!/usr/bin/python3
"""
a Fabric script (based on the file 3-deploy_web_static.py) that deletes out-of-date archives
 using the function do_clea
"""
from fabric.api import local, run, env
env.hosts = ['107.23.168.84', '52.90.109.65']  # list of web servers


def do_clean(number=0):
    """Deleting the  out of date archives"""
    files = local("ls -1t versions", capture=True)
    file_names = files.split("\n")
    n = int(number)
    if n in (0, 1):
        n = 1
    for i in file_names[n:]:
        local("rm versions/{}".format(i))
    dir_server = run("ls -1t /data/web_static/releases")
    dir_server_names = dir_server.split("\n")
    for i in dir_server_names[n:]:
        if i is 'test':
            continue
        run("rm -rf /data/web_static/releases/{}"
            .format(i))