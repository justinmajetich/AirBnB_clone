#!/usr/bin/python3
# Fabfile to create and distribute an archive to a web server.
from fabric import task


@task
def do_pack(c):
    """Create a tar gzipped archive of the directory web_static."""
    dt = c.run("date +'%Y%m%d%H%M%S'", hide=True).stdout.strip()
    file = f"versions/web_static_{dt}.tgz"

    c.run("mkdir -p versions")
    result = c.run(f"tar -cvzf {file} web_static")
    if result.failed:
        return None

    return file

@task
def do_deploy(c, archive_path):
    """Distributes an archive to a web server."""
    if not c.file_exists(archive_path):
        return False

    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    c.put(archive_path, f"/tmp/{file}")
    c.run(f"rm -rf /data/web_static/releases/{name}/")
    c.run(f"mkdir -p /data/web_static/releases/{name}/")
    c.run(f"tar -xzf /tmp/{file} -C /data/web_static/releases/{name}/")
    c.run(f"rm /tmp/{file}")
    c.run(f"mv /data/web_static/releases/{name}/web_static/* /data/web_static/releases/{name}/")
    c.run(f"rm -rf /data/web_static/releases/{name}/web_static")
    c.run(f"rm -rf /data/web_static/current")
    c.run(f"ln -s /data/web_static/releases/{name}/ /data/web_static/current")

    return True

@task
def deploy(c):
    """Create and distribute an archive to a web server."""
    print("Starting deployment...")

    file = do_pack(c)
    if file is None:
        return False

    return do_deploy(c, file)

