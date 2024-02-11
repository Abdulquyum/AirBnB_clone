#!/usr/bin/python3
""" User's state Amenity"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """define modules for state amenities of users"""
    def __init__(self):
        self.name = ""
        super().__init__()
