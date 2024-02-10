#!/usr/bin/python3
"""
This Model contains place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    class that defines the place

    Attributes:
    city_id (str): it will be the City.id
    user_id (str): it will be the user.id
    name (str): the amenity name
    description (str): The description of room
    number_rooms (int): The number of rooms
    number_bathrooms (int): The number of bathrooms
    max_guest (int): The number of guest
    price_by_night (int): Price the room by the night
    latitude (float): latitude of room
    longitude (float): longitude of room
    amenity_ids (list): it will be the list of Amenity.id later
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
