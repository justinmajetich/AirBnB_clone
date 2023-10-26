#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers and deploys it.
"""
from fabric.api import put, run, env
from os.path import exists

env.hosts = ['52.55.249.213', '54.157.32.137']
env.user = "ubuntu"
env.key_filename = "/root/.ssh/school"


def do_deploy(archive_path):
    """Distribute and deploy the archive to web servers."""
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory on the server
        put(archive_path, "/tmp/")

        # Get the archive filename without extension
        filename = archive_path.split("/")[-1].split(".")[0]

        # Uncompress the archive to the /data/web_static/releases/ directory
        run("mkdir -p /data/web_static/releases/{}/".format(filename))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".
            format(filename, filename))

        # Delete the archive from the server
        run("rm /tmp/{}.tgz".format(filename))

        # Move contents to appropriate location
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(filename, filename))
        run("rm -rf /data/web_static/releases/{}/web_static".format(filename))

        # Delete the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s /data/web_static/releases/{}/ "
            "/data/web_static/current".format(filename))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed: {}".format(str(e)))
        return False


if __name__ == "__main__":
    # Replace with the actual path to your web_static archive
    archive_path = "versions/web_static_20170315003959.tgz"
    do_deploy(archive_path)
