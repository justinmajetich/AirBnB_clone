#!/usr/bin/python3
"""
A Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives, using the function do_clean
"""
import os
from fabric.api import cd, env, local, run

env.hosts = ["34.231.110.206", "3.239.57.196"]


def do_clean(number=0):
    """
    Deletes out-of-date archives
    Args:
        number: is the number of the archives, including the most recent
    """
    n = 1 if int(number) == 0 else int(number)
    files = [f for f in os.listdir('./versions')]
    files.sort(reverse=True)
    for f in files[n:]:
        local("rm -f versions/{}".format(f))
    remote = "/data/web_static/releases/"
    with cd(remote):
        tgz = run(
            "ls -tr | grep -E '^web_static_([0-9]{6,}){1}$'"
        ).split()
        tgz.sort(reverse=True)
        for d in tgz[n:]:
            run("rm -rf {}{}".format(remote, d))
