#!/usr/bin/python3
"""
State class, a subclass of BaseModel
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    A subclass of BaseModel class

    Public class attribute:
    name (str): state name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')

    @property
    def cities(self):
        """
        eturns the list of City instances with state_id equals to the current State.id
        """
        from models.engine import file_storage

        all_cities = file_storage.FileStorage.all(self)
        return all_cities
