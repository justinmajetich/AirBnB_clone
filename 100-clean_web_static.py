#!/usr/bin/python3
"""
    a Fabric script (based on the file 3-deploy_web_static.py)
    that deletes out-of-date archives, using the function do_clean:
"""

from fabric.api import *

env.hosts = ['34.203.33.172', '54.210.234.151']

env.user = "ubuntu"


def do_clean(number=0):
    """ Delete unnecessary archives """

    to_keep = 0
    Fpath = "/data/web_static/releases"

    try:
        number = int(number)

        if (number < 0):
            print("Invalid number")
            return (1)

    except Exception:
        print("Wrong value passed")
        return (1)

    # get the number of files to keep
    if number == 0:
        to_keep = 1
    else:
        to_keep = number

    # Delete all unnecessary archives in the local versions folder
    local(f'cd version ; ls -t | tail -n +{to_keep + 1} | xargs rm -rf')

    # Delete all unnecessary archives in the '/data/web_static/releases'
    # folder of both of your web servers
    run(f'cd {Fpath} ; ls -t | tail -n +{to_keep + 1} | xargs rm -rf')
