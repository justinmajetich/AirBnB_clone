#!/usr/bin/python3
from fabric.api import env, local, put
from datetime import datetime
import os.path



env.user = 'ubuntu'
env.hosts = ['54.146.13.194']

def do_pack():
        dt = datetime.utcnow()
        folder = "/root/AirBnB_clone_v2/web_static"
        if os.path.isdir("versions") is False:
            local("mkdir -p versions")
        archive = "/root/AirBnB_clone_v2/web_static/versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

        local(f"tar czf {archive} -C {folder} .")
        return folder
