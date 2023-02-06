"""
BaseModel class
"""
import uuid
from datetime import datetime, date, time


class BaseModel:
    """
    A class that defines all common attributes/methods for other classes

    Attributes
    ----------
    id (str) : unique id for base model
    created_at (datetime) : time of creation for base model
    updated_at (datetime) : time of creation for base model after update
    """
    def __init__(self):
        """
        initializes the class
        """
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.now())
        self.updated_at = str(datetime.now())

    def __str__(self):
        """
        returns the class data in readable format
        """
        data = f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
        return data

    def save(self):
        """
        updates instance attribute saved at with the current datetime
        """
        self.updated_at = str(datetime.now())

    def to_dict(self):
        """
        returns a dictionary containing instance data
        """
        data = self.__dict__
        modified = {}
        # modify dict and change its formatting
        for key, value in data.items():
            # add the __class__ key to dictionaty after the name key
            if key == "name":
                modified["__class__"] = type(self).__name__
            elif key == "updated_at":
                self.save()
                dt = datetime.fromisoformat(self.updated_at)
                modified["updated_at"] = dt
            elif key == "created_at":
                dt = datetime.fromisoformat(self.created_at)
                modified["created_at"] = dt
            else:
                modified[key] = value
                return modified
