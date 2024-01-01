#!/usr/bin/python3
"""
Fabric script that distributes an archive to my web servers
"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ["ubuntu@54.146.95.43", "ubuntu@34.229.67.181"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"

def do_pack():
    """Generates a .tgz archive from contents of web_static."""
    time = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(time)
    try:
        local("mkdir -p ./versions")
        local("tar -czvf {} ./web_static".format(file_name))
    except Exception as e:
        print(e)
        return None
    else:
        return file_name

def do_deploy(archive_path):
    """
    Distributes an archive to your web servers.

    Parameters:
        - archive_path (str): Path to the archive file.

    Returns:
        - True if deployment is successful, else False.
    """
    if os.path.isfile(archive_path) is False:
        return False

    try:
        archive = archive_path.split("/")[-1]
        path = "/data/web_static/releases"
        folder = archive.split(".")
        new_archive = ".".join(folder)

        # Upload the archive to /tmp/ on the server
        put("{}".format(archive_path), "/tmp/{}".format(archive))

        # Create the release directory
        run("mkdir -p {}/{}/".format(path, folder[0]))

        # Extract the archive into the release directory
        run("tar -xzf /tmp/{} -C {}/{}/".format(new_archive, path, folder[0]))

        # Remove the uploaded archive
        run("rm /tmp/{}".format(archive))

        # Move the contents of web_static to the release directory
        run("mv {}/{}/web_static/* {}/{}/"
            .format(path, folder[0], path, folder[0]))

        # Remove the web_static directory in the release directory
        run("rm -rf {}/{}/web_static".format(path, folder[0]))

        # Remove the existing /data/web_static/current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link pointing to the new release directory
        run("ln -sf {}/{} /data/web_static/current".format(path, folder[0]))

    except Exception as e:
        print(e)
        return False
    finally:
        return True

def do_clean(number=0):
    """
    Deletes out-of-date archives.

    Parameters:
        - number (int): Number of archives to keep.

    Returns:
        - None
    """
    number = int(number)

    if number == 0 or number == 1:
        local("ls -t versions/ | tail -n +2 | xargs -I {} rm versions/{}")
        run("ls -t /data/web_static/releases | tail -n +2 | xargs -I {} rm -rf /data/web_static/releases/{}")

    elif number > 1:
        local("ls -t versions/ | tail -n +{} | xargs -I {} rm versions/{}"
              .format(number + 1))
        run("ls -t /data/web_static/releases | tail -n +{} | xargs -I {} rm -rf /data/web_static/releases/{}"
            .format(number + 1))
