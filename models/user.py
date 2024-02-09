#!/usr/bin/python3
""" User class that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    ''' define user class methods '''
    def __init__(self):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__()
