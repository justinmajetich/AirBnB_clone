#!/usr/bin/python3
"""
script (based on the file 3-do_deploy_web_static.py) that deletes
out-of-date archives
"""
import os.path
from fabric.api import *
from fabric.operations import run, put
from datetime import datetime


env.hosts = ['3.227.217.150', '3.95.27.202']
env.user = "ubuntu"


def deploy():
    """creates and distributes an archive to your web servers

    All remote commands must be executed on both of web your servers (using
    env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script).
    You must use this script to deploy it on your servers: xx-web-01 and
    xx-web-02.

    Returns:
        _type_: value of do_deploy
    """
    # Call the do_pack() function and store the path of the created archive
    archive_path = do_pack()
    if archive_path is None:
        print("Failed to create archive from web_static")
        return False

    # Call do_deploy function, using the new path of the new archive and
    # return the return value of do_deploy
    return do_deploy(archive_path)


def do_pack():
    """ generates a .tgz archive from the contents of the web_static

    All files in the folder web_static must be added to the final archive.
    All archives must be stored in the folder versions.
    The name of the archive created must be:
        web_static_<year><month><day><hour><minute><second>.tgz
    The function do_pack must return the archive path if the archive has
    been correctly generated. Otherwise, it should return None.

    Returns:
        fabric.operations._AttributeString: archive path.
    """
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    cur_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        cur_time.year,
        cur_time.month,
        cur_time.day,
        cur_time.hour,
        cur_time.minute,
        cur_time.second
    )
    try:
        print("Packing web_static to {}".format(output))
        # extract the contents of a tar archive
        local("tar -cvzf {} web_static".format(output))
        archize_size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, archize_size))
    except Exception:
        output = None
    return output


def do_deploy(archive_path):
    """distributes an archive to your web servers.

    Args:
        archive_path (string): path to archive

    Returns:
        Boolean: whether the archive is distributed or not
    """
    if not os.path.exists(archive_path):
        return False
    # Uncompress the archive to the folder,
    # /data/web_static/releases/<archive filename without extension>
    # on the web server
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False

    try:
        # upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/{}".format(file_name))

        # Create new directory for release
        run("mkdir -p {}".format(folder_path))

        # Untar archive
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))

        # Delete the archive from the web server
        run("rm -rf /tmp/{}".format(file_name))

        # Move extraction to proper directory
        run("mv {}web_static/* {}".format(folder_path, folder_path))

        # Delete first copy of extraction after move
        run("rm -rf {}web_static".format(folder_path))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create new the symbolic link /data/web_static/current on web server,
        # linked to the new version of your code,
        # (/data/web_static/releases/<archive filename without extension>
        run("ln -s {} /data/web_static/current".format(folder_path))

        print('New version deployed!')
        success = True

    except Exception:
        success = False
        print("Could not deploy")
    return success


def do_clean(number=0):
    """deletes out-of-date archives

    If number is 0 or 1, keep only the most recent version of your archive.
    if number is 2, keep the most recent, and second most recent versions of
    your archive.
    Delete all unnecessary archives (all archives minus the number to keep
    in the versions folder.
    Delete all unnecessary archives (all archives minus the number to keep)
    in the /data/web_static/releases folder of both of your web servers.

    Args:
        number (int, optional): number of the archives, including the most
        recent, to keep. Defaults to 0.
    """
    archives = os.listdir('versions/')
    archives.sort(reverse=True)
    start = int(number)
    path = '/data/web_static/releases'
    if not start:
        start += 1
    if start < len(archives):
        archives = archives[start:]
    else:
        archives = []
    for archive in archives:
        os.unlink('versions/{}'.format(archive))
    cmd_parts = [
        "rm -rf $(",
        "find {}/ -maxdepth 1 -type d -iregex",
        " '{}/web_static_.*'",
        " | sort -r | tr '\\n' ' ' | cut -d ' ' -f{}-)"
        .format(path, path, start + 1)
    ]
    run(''.join(cmd_parts))
