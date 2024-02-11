#!/usr/bin/python3
'''define Users place of stay '''


from models.base_model import BaseModel


class Place (BaseModel):
    '''Modules for the atttributes of place '''
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest: integer = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
