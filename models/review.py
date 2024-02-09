#!/usr/bin/python3
'''User review class'''


from models.base_model import BaseModel


class Review(BaseModel):
    '''Modules to review user activities'''
    def __init__(self):
        self.place_id = ""
        self.user_id = ""
        self.text = ""
