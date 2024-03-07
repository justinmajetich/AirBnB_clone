#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder and distributes it to web servers.
"""
import os
from datetime import datetime

from fabric.api import env, local, put, run

# List of servers to deploy to
env.hosts = ["34.234.193.86", "54.90.40.86"]


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    The archive is stored in the 'versions' folder.
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{timestamp}.tgz"
    archive_path = os.path.join("versions", archive_name)

    # Create 'versions' directory if it doesn't exist
    if not os.path.exists("versions"):
        os.mkdir("versions")

    # Create a .tgz archive of the web_static directory
    local(f"tar -cvzf {archive_path} web_static")

    return archive_path if os.path.exists(archive_path) else None


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Extract filename and name without extension from archive_path
        filename = os.path.basename(archive_path)
        name = filename.split(".")[0]

        # Define remote paths
        remote_tmp_path = f"/tmp/{filename}"
        remote_release_path = f"/data/web_static/releases/{name}/"

        # Upload archive to /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Uncompress the archive to the folder on the web server
        run(f"mkdir -p {remote_release_path}")
        run(f"tar -xzf {remote_tmp_path} -C {remote_release_path}")

        # Delete the archive from the web server
        run(f"rm {remote_tmp_path}")

        # Move files from web_static_* to releases/ folder
        run(f"mv {remote_release_path}web_static/* {remote_release_path}")

        # Delete the now empty web_static_* folder
        run(f"rm -rf {remote_release_path}web_static")

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link /data/web_static/current on the web server
        run(f"ln -s {remote_release_path} /data/web_static/current")

        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
