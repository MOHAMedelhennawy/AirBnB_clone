#!/usr/bin/python3
'''
module that contain BaseModel
'''

from uuid import uuid4
from datetime import datetime


class BaseModel:
    '''
    BaseModel that defines all common attributes/methods for other classes
    '''

    def __init__(self):
        '''
        the initialization of attributes
        '''

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''
        Return the informal presentation of class
        '''

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''
        updates the public instance attribute updated_at with the current datetime
        '''

        self.updated_at = datetime.now()

    def to_dict(self):
        '''
        returns a dictionary containing all keys/values of __dict__ of the instance
        '''

        self.__dict__["__class__"] = self.__class__.__name__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__

if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
