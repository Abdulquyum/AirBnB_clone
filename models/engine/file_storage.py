#!/usr/bin/python3
""" Storage class definition """


import json


class FileStorage():
    ''' Modules to help in saving, serialization of instances
    to a JSON file and deserializes JSON file to instances'''
    def __init__(self):
        self.__file_path = ""
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        obj = BaseModel()
        self.__objects = obj.id

    def save(self):
        try:
            with open("file.json", 'w') as f:
                f.write(json.dumps(self.__objects))
        except Exception as s:
            pass

    def reload(self):
        try:
            with open("file.json", 'r') as f:
                return json.load(f)
        except Exception as s:
            pass
