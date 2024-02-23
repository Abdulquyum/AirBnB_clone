#!/usr/bin/python3
'''User review class'''


from models.base_model import BaseModel


class Review(BaseModel):
    '''Modules to review user activities'''
    place_id = ""
    user_id = ""
    text = ""
