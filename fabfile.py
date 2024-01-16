#!/usr/bin/python3

from fabric import Connection

c = Connection(host='ubuntu@52.87.231.155', connect_kwargs={"password": "~/.ssh/id_rsa"})
# Create a directory (i.e. folder)
# Hostname

re = c.local("hostname")
# Capture the output of "ls" command
# Check if command failed
print(re.failed)