#!/usr/bin/python3

"""
File storage class
"""


import json


class FileStorage:
    """
    file storage class serializes instance to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """
        serialize __objects to JSON file path
        """
        # modify self.__objects
        json_objects = {}
        with open(FileStorage.__file_path, mode="w+", encoding="utf-8") as f:
            for key, value in FileStorage.__objects.items():
                json_objects[key] = value.to_dict()
            json.dump(json_objects, f)


    def reload(self):
        """
        deserialize the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                dict = json.loads(f.read())
                for value in dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except:
            pass
