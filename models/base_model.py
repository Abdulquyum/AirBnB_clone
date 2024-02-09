#!/usr/bin/python3
""" Base Model class of my AirBnB project
    defines all common attributes/methods for other classes"""


from datetime import datetime
import uuid


class BaseModel():
    """ Contain all modules to aid the
    perfect execution of the project """
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        date_now = datetime.now()
        self.created_at = date_now.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = date_now.strftime("%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        date_now = datetime.now()
        self.updated_at = datetime.strftime(date_now, "%Y-%m-%dT%H:%M:%S.%f")

    def to_dict(self):
        obj_dict = self.__dict__
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict

    def save(self):
        date_now = datetime.now()
        self.updated_at = datetime.strftime(date_now, "%Y-%m-%dT%H:%M:%S.%f")
