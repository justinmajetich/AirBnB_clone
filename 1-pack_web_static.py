#!/usr/bin/python3
# Compress before sending
"""Compress usign fabric"""
from fabric.api import local
import datetime


def do_pack():
    """compress function"""
    try:
        local("mkdir -p versions")
        date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(date))
        return "versions/web_static_{}.tgz web_static_{}".format(date)
    except Exception:
        return None
