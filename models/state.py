#!/usr/bin/python3
""" User's state """


from models.base_model import BaseModel


class State(BaseModel):
    """define modules for state of users"""
    def __init__(self):
        self.name = ""
