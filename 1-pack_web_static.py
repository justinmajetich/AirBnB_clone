#!/usr/bin/python3
"""script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """ generates a .tgz archive from the contents of the web_static

    All files in the folder web_static must be added to the final archive.
    All archives must be stored in the folder versions.
    The name of the archive created must be:
        web_static_<year><month><day><hour><minute><second>.tgz
    The function do_pack must return the archive path if the archive has
    been correctly generated. Otherwise, it should return None.

    Returns:
        fabric.operations._AttributeString: archive path.
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")

    # create folder versions if it doesn’t exist
    local("mkdir -p versions")

    # extract the contents of a tar archive
    result = local("tar -czvf versions/web_static_{}.tgz web_static"
                   .format(now))
    if result.failed:
        return None
    else:
        return result

if __name__ == "__main__":
    do_pack()
