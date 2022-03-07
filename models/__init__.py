#!/usr/bin/python3
"""This module instantiates an object to respective storage"""
if HBNB_TYPE_STORAGE == db:
	from models.engine.db_storage import DBStorage
	storage = DBStorage()
else:
	from models.engine.file_storage import FileStorage
	storage = FileStorage()

storage.reload()
