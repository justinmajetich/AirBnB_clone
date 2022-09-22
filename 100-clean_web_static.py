#!/usr/bin/python3
# Full deploy with do_clean function
from fabric.api import env, sudo, local

env.hosts = ['34.202.231.144', '54.85.119.117']
env.user = 'ubuntu'


def do_clean(number=0):
    """Cleans old versions from local and remote folders

    Args:
        number (str): number of the archives to keep (the newest)
    """
    number = int(number)
    if number == 0:
        number = 1
    list_files = []
    code = "ls -ltr versions | rev | cut -d ' ' -f1 | rev"
    value = local(code, capture=True)
    for line in value.splitlines():
        if line.startswith('web_static'):
            list_files.append(line)
    for i in range(len(list_files) - number):
        local("rm versions/{}".format(list_files[i]))
    # For remote servers
    r_list_files = []
    r_code = "ls -ltr /data/web_static/releases | rev | cut -d ' ' -f1 | rev"
    r_value = sudo(r_code)
    for line in r_value.splitlines():
        if line.startswith('web_static'):
            r_list_files.append(line)
    for i in range(len(r_list_files) - number):
        sudo("rm -rf /data/web_static/releases/{}".format(r_list_files[i]))
