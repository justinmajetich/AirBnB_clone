#!/usr/bin/python3
"""that deletes out-of-date archives, using the function do_clean"""
from fabric.api import env, put, run
from datetime import datetime
from os import listdir

env.host = ['52.91.116.127', '100.25.45.223']
env.user = 'ubuntu'

def sort_list(item):
    return int(item.split('_')[-1])

def do_clean(number=0):
    # sorting_function = lambda item: int(item.split('_')[-1])
    if number < 0:
        return
    elif number == 0:
        number = 1
    versions_content = [item.split('.')[0] for item in listdir("versions")]
    releases_content = [item.split('.')[0] for item in listdir("/data/web_static/releases")]
    # s_versions_content = versions_content.sort(key=sort_list)
    # s_releases_content = releases_content.sort(key=sort_list)
    if len(versions_content) >= number:
        for static in versions_content[:-number]:
            run("rm {}.tgz".format(static))
    if len(releases_content) >= number:
        for static in releases_content[:-number]:
            run("rm /data/web_static/releases/{}.tgz".format(static))
