#!/usr/bin/python3
"""
Keep it clean!
"""
from fabric.api import env, cd, run, local
import os

env.hosts = ["34.231.110.206", "3.239.57.196"]

def do_clean(number=0):
    """
    Fabric script (based on the file 3-deploy_web_static.py)
    that deletes out-of-date archives, using the function do_clean
    """
    cl = 1 if int(number) == 0 else int(number)
    archieve = [do for do in os.listdir('./versions')]
    archieve.sort(reverse=True)

    while cl < len(archieve):
        do = archieve[cl]
        local("rm -do versions/{}".format(do))
        cl += 1

    remote = "/data/web_static/releases/"

    with cd(remote):
        tgz = run(
            "ls -tr | grep -E '^web_static_([0-9]{6,}){1}$'"
        ).split()
        tgz.sort(reverse=True)

        while cl < len(tgz):
            d = tgz[cl]
            run("rm -rf {}{}".format(remote, d))
            cl += 1
