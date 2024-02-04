from fabric.api import *
from datetime import datetime
from os.path import exists, join

env.hosts = ['54.146.59.198', '54.85.84.184']
env.user = 'Lavyatarah'
env.key_filename = '/usr/laven/Desktop/practice folder/node_module'

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
