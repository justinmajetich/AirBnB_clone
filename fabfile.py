#!/usr/bin/python3

from fabric import Connection

c = Connection(host='ubuntu@52.87.231.155', connect_kwargs={"key_filename": "~/.ssh/id_rsa"})
