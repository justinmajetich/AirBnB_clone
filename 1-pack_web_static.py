from fabric import Connection
import datetime
import os

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    of the AirBnB Clone repo.
    """
    # Create the versions folder if it doesn't exist
    if not os.path.exists('versions'):
        os.makedirs('versions')

    # Get the current date and time
    now = datetime.datetime.now()
    timestamp = now.strftime('%Y%m%d%H%M%S')

    # Create the archive name
    archive_name = f'web_static_{timestamp}.tgz'
    archive_path = os.path.join('versions', archive_name)

    # Create the .tgz archive
    with Connection('localhost') as c:
        c.run(f'tar -czvf {archive_path} web_static')

    # Return the archive path
    return archive_path
