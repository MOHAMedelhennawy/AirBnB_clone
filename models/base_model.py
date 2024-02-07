#!/usr/bin/python3
'''
module that contain BaseModel
'''

from uuid import uuid4
from datetime import datetime
from models.__init__ import storage

class BaseModel:
    '''
    BaseModel that defines all common attributes/methods for other classes
    '''

    def __init__(self, *args, **kwargs):
        '''
        the initialization method of attributes
        '''

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        storage.new(self)

    def __str__(self):
        '''
        Return the informal presentation of class
        '''

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''
        updates the public instance attribute updated_at
        with the current datetime
        '''

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''
        returns a dictionary containing all keys/values of
        __dict__ of the instance
        '''

        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict
