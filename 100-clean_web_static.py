#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder and distributes it to web servers.
"""
import os
from datetime import datetime

from fabric.api import env, local, put, sudo, task
from fabric.decorators import runs_once

# List of servers to deploy to
env.hosts = ["34.234.193.86", "54.90.40.86"]


@runs_once
def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    The archive is stored in the 'versions' folder.
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{timestamp}.tgz"
    archive_path = os.path.join("versions", archive_name)

    # Create 'versions' directory if it doesn't exist
    os.makedirs("versions", exist_ok=True)

    # Create a .tgz archive of the web_static directory
    print(f"Packing web_static to {archive_path}")
    result = local(f"tar -cvzf {archive_path} web_static", capture=False)

    if result.return_code == 0:
        size = os.path.getsize(archive_path)
        print(f"web_static packed: {archive_path} -> {size}Bytes")
        return archive_path

    return None


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        archive_name = os.path.basename(archive_path)
        archive_name_no_ext = archive_name.split(".")[0]
        release_dir = f"/data/web_static/releases/{archive_name_no_ext}"

        # Uncompress the archive to the folder /data/web_static/releases/
        sudo(f"mkdir -p {release_dir}")
        sudo(f"tar -xzf /tmp/{archive_name} -C {release_dir}")

        # Copy the contents of web_static to the parent directory
        sudo(f"rsync -a {release_dir}/web_static/ {release_dir}/")

        # Remove the now empty web_static directory
        sudo(f"rm -rf {release_dir}/web_static")

        # Delete the archive from the web server
        sudo(f"rm -rf /tmp/{archive_name}")

        # Delete the symbolic link /data/web_static/current from the web server
        sudo("rm -rf /data/web_static/current")

        # Create a new the symbolic link /data/web_static/current on server
        # linked to the new version of your code
        sudo(f"ln -s {release_dir} /data/web_static/current")

        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """
    Creates and distributes an archive to your web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


@task(default=True)
def do_clean(number=0):
    """
    Deletes out-of-date archives.
    """
    number = int(number)

    # Keep at least one version if number is less than 1
    if number < 1:
        number = 1

    try:
        # Delete local archives
        local_archives = sorted(os.listdir("versions"))[:-number]
        for archive in local_archives:
            local(f"rm versions/{archive}")

        # Delete remote archives
        command = (
                "for dir in $(ls -1t /data/web_static/releases/ | "
                f"tail -n +{number + 1}); do "
                "rm -rf /data/web_static/releases/$dir; "
                "done"
                )
        sudo(command)

        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
