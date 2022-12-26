#!/usr/bin/python3
"""
compress before sending
"""
from fabric.api import local


def do_pack():
	"""generates an archive"""
	myVar = var()
	local(tar -czvf my)
