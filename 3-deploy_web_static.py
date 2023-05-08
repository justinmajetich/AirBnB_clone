#!/usr/bin/python3
# A module that do full deployment
from fabric.api import local, env, put, run
from datetime import datetime
import os


env.hosts = ['18.206.207.43', '100.26.50.89']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """ Creating the archive name """
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = "web_static_" + timestamp + ".tgz"

    # Creating the folder if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Creating the archive
    archive = local("tar -cvzf versions/{} web_static".format(archive_name))

    # Returning the archive path if the archive is correctly generated,
    # otherwise it should return None
    if archive.failed:
        return None

    return "versions/web_static_{}.tgz".format(timestamp)


def do_deploy(archive_path):
    """Distributes an archive to web servers

    Args:
        archive_path (str): path to the archive file

    Return: True if all operations have been done correctly
            otherwise returns False
    """
    # check if the archive path does exist
    if not os.path.exists(archive_path):
        return False
    # Get the archive name without its extension (.tgz)
    archive_name = archive_path.split("/")[-1]
    archive_name_no_extension = archive_name.split(".")[0]
    # Uncompress the archive to
    # /data/web_static/releases/archive_name_no_extension
    destined_folder = "/data/web_static/releases/{}/"\
                      .format(archive_name_no_extension)

    # Returns True if all operations have been done correctly,
    # otherwise returns False
    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        # Create a directory where it should be uncompressed
        run("mkdir -p {}".format(destined_folder))
        # Uncompress to the destined directory
        run("tar -xzf /tmp/{} -C {}".format(archive_name, destined_folder))
        # Delete the uploded archive (in /tmp/ directory)
        run("rm /tmp/{}".format(archive_name))
        # Move all files inside web_static to the destined_folder created
        run("mv {}web_static/* {}".format(destined_folder, destined_folder))
        # Delte the empty web_static folder
        run("rm -rf {}web_static".format(destined_folder))
        # Delete the symbolic link
        run("rm -rf /data/web_static/current")
        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(destined_folder))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """Creates and distributes an archive to my web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
