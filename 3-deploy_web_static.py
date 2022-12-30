#!/usr/bin/python3
# Full deployment
from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy

env.hosts = [18.215.160.48, 34.201.174.39]


def deploy():
	"""Based on 2 and Based on 1"""
	archive_path = do_pack()
	if not archive_path:
		return False
	new_deploy = do_deploy(archive_path)
	return new_deploy
