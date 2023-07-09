from fabric import task, Connection, Config, SerialGroup
from invoke import Collection

@task
def upload(ctx):
    with Connection('ubuntu@54.146.78.93') as conn:
        conn.put('testtransfer', '~/')
        print("File uploaded successfully!")

@task
def download_file(ctx):
    with Connection('your_username@your_server_ip') as conn:
        conn.get('/remote/path/remote_file.txt', 'local_directory/')
        print("File downloaded successfully!")

collection = Collection()
collection.add_task(upload)
collection.add_task(download_file)

