#!/usr/bin/python3
""" User's city """


from models.base_model import BaseModel


class City(BaseModel):
    """ Modules defining users city """
    def __init__(self):
        state_id = ""
        self.name = ""
        super().__init__()
