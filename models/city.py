#!/usr/bin/python3
"""
This Model contains city class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    class that defines the city

    Attributes:
    state_id(str): the state_id
    name (str): the city name
    """
    state_id = ''
    name = ''
