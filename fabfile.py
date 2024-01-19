#!/usr/bin/python3

from fabric import Connection
from fabric.api import *
c = Connection(host='ubuntu@54.237.91.183', connect_kwargs={"password": "~/.ssh/id_rsa"})
