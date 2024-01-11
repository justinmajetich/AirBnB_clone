#!/usr/bin/python3
"""a Fabric script (based on the file 2-do_deploy_web_static.py)
    that creates and distributes an archive to your web servers,
    using the function deploy:"""

from os.path import exists, isdir
from datetime import datetime
from fabric.api import put, run, env, local
env.hosts = ['54.237.84.15', '3.89.155.134']



def do_pack():
    """Generate a .tgz archive from
        e contents of web_static folder"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        fileName = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(fileName))
        return fileName
    except:
        return None


def do_deploy(archive_path):
    """Ditributes an archive file to my web server"""
    if exists(archive_path) is False:
        return False
    try:
        path = "/data/web_static/releases/"
        fileName = archive_path.split("/")[-1]
        noExtFile = fileName.split(".")[0]
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, noExtFile))
        run('tar -xzf /tmp/{} -C {}{}/'.format(fileName, path, noExtFile))
        run('rm /tmp/{}'.format(fileName))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, noExtFile))
        run('rm -rf {}{}/web_static'.format(path, noExtFile))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, noExtFile))
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
