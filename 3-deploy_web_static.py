#!/usr/bin/python3
"""
Fabric script that creates and
distributes an archive to the web servers
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['34.204.50.206', '3.93.60.31']
def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if not exists(archive_path):
        return False
    try:
        archive_file = archive_path.split("/")[-1]
        release_f = "/data/web_static/releases/".format(archive_file.split(".")[0])
        put(archive_path, '/tmp/')
        run('mkdir -p {}/'.format(release_f))
        run('tar -xzf /tmp/{} -C {}/'.format(archive_file, release_f))
        run('rm /tmp/{}'.format(archive_file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(release_f))
        run('rm -rf {}/web_static'.format(release_f))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/ /data/web_static/current'.format(release_f))
        return True
    except:
        return False
def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
