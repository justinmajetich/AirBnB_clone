from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['54.146.59.198', '54.85.84.184']  # <IP web-01>, <IP web-02>

def do_deploy(archive_path):
    """ Distributes an archive to web servers and deploys it """
    if not exists(archive_path):
        return False

    filename = archive_path.split('/')[-1]
    no_tgz = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])
    # curr = '/data/web_static/current'
    tmp = "/tmp/" + filename

    try:
        put(archive_path, "/tmp/")
        # ^ Upload the archive to the /tmp/ directory of the web server
        run("mkdir -p {}".format(no_tgz))
        # Uncompress the archive to the folder /data/web_static/releases/
        # <archive filename without extension> on the web server
        run("tar -xzf /tmp/{} -C {}/".format(filename, no_tgz))
        run("rm /tmp/{}".format(filename))
        run("mv {}/* {}/".format(no_tgz, no_tgz))
        run("rm -rf {}/web_static".format(no_tgz))
        # ^ Delete the archive from the web server
        run("rm /data/web_static/current")
        # Delete the symbolic link /data/web_static/current from the web server
        run("ln -s {} /data/web_static/current".format(no_tgz))
        # Create a new the symbolic link /data/web_static/current on the
        # web server, linked to the new version of your code
        # (/data/web_static/releases/<archive filename without extension>)
        return True
    except:
        return False
