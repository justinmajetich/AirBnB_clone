from fabric.api import *
from datetime import datetime
from os.path import exists, join

env.hosts = ['<54.146.59.198>', '<54.85.84.184>']
env.user = 'Lavyatarah'
env.key_filename = 'AAAAB3NzaC1yc2EAAAADAQABAAABAQDW0NEnqaWfJ4Uh6uUZf0GA+2zrMSGymZ0LxC37pptctbg15TJN8qOG+VzMI8UCNaGo64nteBPBq2i6v9AzFEQ8MdF+2EX7zF8csoPOwiUoOt1NZ4h361iz/WmOjyqbrdCf3d1aTpj11wpsUUR/nAXlZbUfrP8eQscfzYCeWir1f/aeNKgwd7eJrBYzjftDW2zPL5ioaaJLWpQMNbTBjFpJdFbVHbn7PVOv2QQNy98VyqFz352E0FbbbVU8BFbTqGfCHfjOgcG0XaqR2DvFvlKAXVdUZLwMlsQ5mc3vofb4HW8Ok3/Lt2d+b6RXG96DbtFNlNpectGP3v6uYAA9r92J'

def do_clean(number=0):
    """ Deletes out-of-date archives
    """
    # Get the current timestamp
    current_ts = int(datetime.now().timestamp())

    # Get the list of archives in the versions folder
    archives = local("ls /path/to/versions", capture=True).split()

    # Keep only the most recent 'number' archives
    keep_archives = sorted(archives, reverse=True)[:number]

    # Delete the out-of-date archives
    for archive in archives:
        if archive not in keep_archives:
            local("rm /path/to/versions/{}".format(archive))
            run("rm /data/web_static/releases/{}".format(archive))

    # Delete any remaining directories in /data/web_static/releases
    run("find /data/web_static/releases -type d -empty -delete")

    return True
