#!/usr/bin/python3
"""This module imports files from engine"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
