#!/usr/bin/python3
# This fabfile deletes out-of-date archives.
import os
from fabric.api import *

env.hosts = ['34.207.188.42', '54.237.31.63']


def do_clean(number=0):
    """function that deletes out-of-date archives.

    Args:
        number (int): The number of archives to keep.

    If number is 0 or 1, keeps only the most recent of your archive.
    If number is 2, keeps the most and second-most recent versions of archives,
    etc.
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
