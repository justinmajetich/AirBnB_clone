#!/usr/bin/python3
"""pack_web_static
Generate a .tgz archive from static web files
"""
import os
from datetime import datetime
from fabric.api import local, put, run, cd, env, lcd

env.hosts = ['18.207.234.107', '54.197.98.181']


def do_pack():
    """Generate a .tgz archive from the content of `web_static` folder.

    :return: the path of the created archive of None if the archive is missing
    :rtype: string
    """

    if not os.path.exists("versions"):
        os.mkdir("versions")
    archive = (
        "versions/web_static_"
        f"{datetime.now().strftime('%Y%m%d%H%M%S')}.tgz")
    print(f"Packing web_static to {archive}")
    local(f"tar -cvzf {archive} web_static")

    if os.path.exists(archive):
        archive_size = os.path.getsize(archive)
        print(f"web_static packed: {archive} -> {archive_size} Bytes")
        return os.path.abspath(archive)
    else:
        return None


def do_deploy(archive_path):
    """Distribute an archive to a list of web servers.

    :param archive_path: path to the archive to send to the servers
    :type archive_path: str
    :return: True if all operations have been done correctly, otherwise False
    :rtype: bool
    """

    if not os.path.exists(archive_path):
        return False

    status = put(archive_path, '/tmp/')
    archive = os.path.basename(archive_path)
    archive_folder = os.path.splitext(archive)[0]

    if not status.succeeded:
        return False

    with cd('/data/web_static/'):
        status = run(f"mkdir -p /data/web_static/releases/{archive_folder}")
        if not status.succeeded:
            return False
        status = run(f"tar -xzf /tmp/{archive}"
                     f" -C /data/web_static/releases/{archive_folder}")
        if not status.succeeded:
            return False
        status = run(f"rm /tmp/{archive}")
        if not status.succeeded:
            return False
        status = run(
            f"cp -R /data/web_static/releases/{archive_folder}/web_static/*"
            f" /data/web_static/releases/{archive_folder}/")
        if not status.succeeded:
            return False
        status = run(
            f"rm -rf /data/web_static/releases/{archive_folder}/web_static/")
        if not status.succeeded:
            return False
        status = run("rm -rf /data/web_static/current")
        if not status.succeeded:
            return False
        status = run(f"ln -s /data/web_static/releases/{archive_folder}"
                     f" /data/web_static/current")
        if not status.succeeded:
            return False
        print("New version deployed!")


def deploy():
    """Create and distribute an archive to web server"""
    archive = do_pack()

    if archive is None:
        return False
    return(do_deploy(archive))


def do_clean(number=0):
    """Delete out-of-date archives"""
    num = int(number)

    with lcd('versions/'):
        if num == 0 or num == 1:
            local(f"ls -lt | grep -o 'web_static.*' | sed '1,1d' | "
                  f"xargs rm -rf")
        elif num > 1:
            local(f"ls -lt | grep -o 'web_static.*' | sed '1,{num}d' | "
                f"xargs rm -rf")

    with cd('/data/web_static/releases/'):
        if num == 0 or num == 1:
            run(f"ls -lt | grep -o 'web_static.*' | sed '1,1d' | xargs rm -rf")
        elif num > 1:
            run(f"ls -lt | grep -o 'web_static.*' | sed '1,{num}d' | "
                f"xargs rm -rf")
