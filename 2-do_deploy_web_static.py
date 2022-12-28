#!/usr/bin/python3
"""
Deploy archive
"""
import os
from fabric.operations import run, put, sudo
from fabric.api import env
env.user = 'ubuntu'
env.hosts = ['18.215.160.48','34.201.174.39']
env.key_filename = '~/id_rsa'


def do_deploy(archive_path):
	"""A fabric script that distributes archive to your web servers"""
	if os.path.exists(archive_path) is False:
		return False
	try:
		put('archive_path', '/tmp')
		archive = archive_path.split('/')[-1]
		free = archive.strip('.tgz')
		run('mkdir -p /data/web_static/releases/{}/'.format(free))
		run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(archive_path, free))
		run('rm /tmp/{}'.format(archive_path))
		run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}'.format(free, free))
		run('rm -rf /data/web_static/releases/{}/web_static'.format(free))
		run('rm -rf /data/web_static/current')
		run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(free))
		return True
	except:
		return False
