#!/usr/bin/python3
"""
Module that contain FileStorage class
"""
import json
from os import path


class FileStorage:
    """
    Class that serializes instances to a JSON file
    and deserializes JSON file to instances

    Attributes:
    __file_path(string): a path to json file
    __objests(dictionary): dictionary of objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id

        Args:
        obj: object to be added to the dictionary
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        # dict = {}
        # for key, obj in self.__objects.items():
        #     dict[key] = obj.to_dict()

        # with open(self.__file_path, 'w') as f:
        #     f.write(dumps(dict))

        with open(self.__file_path, 'w') as file_obj:
            json.dump(self.__objects, file_obj)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file_obj:
                self.__objects = json.load(file_obj)

