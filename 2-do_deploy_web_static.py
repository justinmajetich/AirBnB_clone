#!/usr/bin/python3
"""
script that distributes archive to webservers
"""
import os.path
from fabric.api import *
from fabric.operations import run, put, sudo

env.hosts = ['100.25.19.204', '54.157.159.85']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/alx_server'

def do_deploy(archive_path):
    """ This function distributes an archive to your web servers"""
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        new_comp = archive_path.split("/")[-1]
        new_folder = ("/data/web_static/releases/" + new_comp.split(".")[0])

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Uncompress the archive to the folder /data/web_static/releases/<archive filename
        # without extension> on the web server
        run("sudo mkdir -p {}".format(new_folder))
        run("sudo tar -xzf /tmp/{} -C {}".
            format(new_comp, new_folder))

        # Delete the archive from the web server
        run("sudo rm /tmp/{}".format(new_comp))

		# move contents into host web_static
        run("sudo mv {}/web_static/* {}/".format(new_folder, new_folder))
        
        # remove extraneous web_static dir
        run("sudo rm -rf {}/web_static".format(new_folder))

        # Delete the symbolic link /data/web_static/current from the web server
        run('sudo rm -rf /data/web_static/current')

        # Create a new the symbolic link /data/web_static/current on the web server,
        # linked to the new version of your code (/data/web_static/releases/<archive filename without extension>)
        run("sudo ln -s {} /data/web_static/current".format(new_folder))

        return True
    except:
        return False
