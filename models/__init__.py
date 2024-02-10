#!/usr/bin/python3
'''Init module '''


import json
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
