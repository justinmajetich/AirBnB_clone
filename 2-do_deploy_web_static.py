#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack."""

from fabric.api import env

env.hosts = ['54.236.217.62', '100.26.229.89']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    '''Function that generates a .tgz archive from the contents of the
    web_static folder.'''
    from fabric.api import local
    from datetime import datetime
    print("Packing web_static to versions/web_static_20170314233357.tgz")
    local('mkdir -p versions')
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file = f"versions/web_static_{date}.tgz"
    try:
        local(f'tar -cvzf {file} web_static')
        return file
    except Exception:
        return None


def do_deploy(archive_path):
    from fabric.api import put, run
    from os.path import exists
    """Deploy web files to server
    """
    try:
        if not (exists(archive_path)):
            return False

        print(f"{run('hostname -I')}Executing task 'do_deploy'")
        # upload archive
        print(f"{run('hostname -I')} put: {archive_path} -> \
/tmp/{archive_path}")
        put(archive_path, '/tmp/')

        # create target dir
        timestamp = archive_path[-18:-4]
        print(f"{run('hostname -I')} run: sudo mkdir -p /data/web_static/\
releases/web_static_{timestamp}/")
        run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(timestamp))

        # uncompress archive and delete .tgz
        print(f"{run('hostname -I')} run: sudo tar -xzf /tmp/{archive_path} \
-C /data/web_static/releases/web_static_{timestamp}/")
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'
            .format(timestamp, timestamp))

        # remove archive
        print(f"{run('hostname -I')} run: sudo rm /tmp/{archive_path}")
        run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

        # move contents into host web_static
        print(f"{run('hostname -I')} run: sudo mv /data/web_static/\
releases/web_static_{timestamp}/web_static/* /data/web_static/releases/\
web_static_{timestamp}/")
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

        # remove extraneous web_static dir
        print(f"{run('hostname -I')} run: sudo rm -rf /data/web_static/\
releases/web_static_{timestamp}/web_static")
        run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'
            .format(timestamp))

        # delete pre-existing sym link
        print(f"{run('hostname -I')} run: sudo rm -rf /data/web_static/\
current")
        run('sudo rm -rf /data/web_static/current')

        # re-establish symbolic link
        print(f"{run('hostname -I')} run: sudo ln -s /data/web_static/\
releases/web_static_{timestamp}/ /data/web_static/current")
        run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(timestamp))
    except Exception:
        return False
    # return True on success
    print(f"{run('hostname -I')} New version deployed!")
    return True
