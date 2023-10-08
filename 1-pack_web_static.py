#!/usr/bin/python3
# fabric script that creat an archeive of the web_static dir

from datetime import datetime
from fabric.api import local


def do_pack():
    """
    archieving web_static dir
    """
#   create  versions directory if not exits
    local("mkdir -p versions")

    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"web_static_{date}.tgz"
    result = local(f"tar -czvf {file_name} web_static ")
    local(f"mv {file_name} ./versions")
#   checking if success

    if result.succeeded:
        return f"versions/{file_name}"
    else:
        return None


if __name__ == "__main__":
    do_pack()
