#!/usr/bin/python3
from fabric.api import local


def do_poo():
    """generates a tgz archive"""
    try:
        local("echo poo")
    except Exception as e:
        return None
