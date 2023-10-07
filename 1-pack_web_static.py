#!/usr/bin/python3
"""generate .tgz archive from contents of web_static folder"""

import fabric.api
from os.path import isdir
import os
from datetime import datetime

def do_pack():
    """use fabric to generate a .tgz file from the given directory"""
    if isdir('versions') is False:
        os.mkdir('versions')
    time_stamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = "versions/webstatic_" + time_stamp + ".tgz"
    fabric.api.local(
        "tar -cvzf " + file_name + " web_static "
        )
    return file_name
