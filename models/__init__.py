#!/usr/bin/python3
"""
this is the init module

"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
