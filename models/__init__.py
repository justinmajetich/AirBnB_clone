#!/usr/bin/python3
"""
Resources for this package

This module instantiates an object of class FileStorage
"""

# Create a unique FileStorage instance for this application
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
