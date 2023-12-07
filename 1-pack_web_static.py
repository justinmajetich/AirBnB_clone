#!/usr/bin/python3
# fabdile to generate

import os.path
from fabric.api import env, local, put
from datetime import datetime



def do_pack():
        dt = datetime.utcnow()
        folder = "/root/AirBnB_clone_v2/web_static"
        if os.path.isdir("versions") is False:
            local("mkdir -p versions")
        archive = "/root/AirBnB_clone_v2/web_static/versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

        local(f"tar czf {archive} -C {folder} .")
        return folder
