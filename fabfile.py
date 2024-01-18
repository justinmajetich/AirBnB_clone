#!/usr/bin/python3

from fabric import Connection

c = Connection(host='f4e06185cedc@f4e06185cedc.3d34c52b.alx-cod.online', connect_kwargs={"password": "7471a2378abbb4545797"})
# Define the remote and local paths
remote_path = "/home"
local_path = "/home/wala/AirBnB_clone_v2/1-pack_web_static.py"

# Use the get method to download files from the remote host to the local machine
re = c.put(remote=remote_path, local=local_path)