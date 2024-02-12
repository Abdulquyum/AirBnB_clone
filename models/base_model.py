#!/usr/bin/python3
""" Base Model class of my AirBnB project
    defines all common attributes/methods for other classes"""


from datetime import datetime
import uuid
from models import storage


class BaseModel():
    """ Contain all modules to aid the
    perfect execution of the project """
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        date_now = datetime.now()
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.created_at = date_now.strftime(date_format)
        self.updated_at = date_now.strftime(date_format)
        if len(kwargs):
            for key, value in kwargs.items():
                if key in ["creted_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(value, date_format)
                else:
                    self.__dict__[key] = value
        # else:
            # self.models.new(self)

    def __str__(self):
        return f"{[__class__.__name__]} {(self.id)} {self.__dict__}"

    def save(self):
        date_now = datetime.now()
        self.updated_at = datetime.strftime(date_now, "%Y-%m-%dT%H:%M:%S.%f")

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict

    def save(self):
        date_now = datetime.now()
        self.updated_at = datetime.strftime(date_now, "%Y-%m-%dT%H:%M:%S.%f")
        storage.save
