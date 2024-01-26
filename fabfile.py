#!/home/wala/AirBnB_clone_v2/venv/bin/python3
from fabric.api import run, env, task

env.hosts = ['54.237.91.183', '54.173.37.227']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def ls():
    run("uname")

# Run the task
