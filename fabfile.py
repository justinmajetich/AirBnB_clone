#!/usr/bin/python3

from fabric import Connection
from fabric import task

@task
def uname(c):
    c = Connection(host='ubuntu@52.87.231.155', connect_kwargs={"password": "~/.ssh/id_rsa"})
    r = c.run('uname -s')

