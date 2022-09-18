#!/usr/bin/python3
"""from models.engine.db_storage import DBStorage"""
from models.engine.file_storage import FileStorage
from os import getenv
"""This module instantiates an object of class FileStorage"""


storage_t = getenv("HBNB_TYPE_STORAGE")
if storage_t == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
