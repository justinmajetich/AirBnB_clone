#!/usr/bin/python3
""" Fabscript that deletes
    out-of-date archives.
"""
import os
from fabric.api import *

env.hosts = ["54.174.230.101", "100.26.57.164"]


def do_clean(number=0):
    """
        Function to delete out-of-date archives
        Args:
        number (int): number of archives to keep
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
