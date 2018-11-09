#!/usr/bin/python3
"""A class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances"""

from models.base_model import BaseModel
import json

class FileStorage:
    """Represents a class FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Class Instantiation"""
        pass

    def all(self):
        """Returns a dictionary"""
        return self.__objects

    def new(self, obj):
        """sets in objects"""
        type(self).__objects = {type(obj).__name__ + '.'+ obj.id: obj}

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        type(self).__objects[type(obj).__name__ + '.'+ obj.id].BaseModel.to_dict()
        with open(FileStorage.__file_path, "w") as write_file:
            json_string = json.dump(type(self).__objects, write_file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as read_file:
                data = json.load(read_file)
        except FileNotFoundError:
            pass
