#!/usr/bin/python3
""" Fabfile that create a .tgz archive from
the contents of web_static folder"""

# if __name__ == '__main__':
from fabric.api import local
from datetime import datetime


def do_pack():
    """Pack all the contents in the web_static directory
    as a tar archive"""

    try:
        local("mkdir -p versions")
        time = datetime.now()
        date_string = '%Y%m%d%H%M%S'
        date = time.strftime(date_string)

        file_path = "versions/web_static_{}.tgz".format(date)
        local("tar -czvf {} web_static".format(file_path))
        return file_path

    except Exception:
        return None
