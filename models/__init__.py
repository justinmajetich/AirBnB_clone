#!/usr/bin/python3
"""
module executes whn models package is imported
"""


from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
