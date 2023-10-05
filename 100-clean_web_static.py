#!/usr/bin/python3
""" Keep it clean!"""
from fabric.api import env, run, local
from os.path import exists
env.hosts = ['<IP web-01>', '<IP web-02>']


def do_clean(number=0):
    """Deletes out-of-date archives"""
    if number == 0 or number == 1:
        number = 1
    else:
        number = int(number)

    with cd('/data/web_static/releases'):
        local("ls -t | tail -n +{} | xargs rm -rf".format(number + 1))

    with cd('/data/web_static/releases'):
        run("ls -t | tail -n +{} | xargs rm -rf".format(number + 1))

    with cd('/versions'):
        local("ls -t | tail -n +{} | xargs rm -rf".format(number + 1))

    with cd('/versions'):
        run("ls -t | tail -n +{} | xargs rm -rf".format(number + 1))
