#!/usr/bin/python3
"""creates a unique file storaage for Application"""


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import review


storage = FileStorage()
storage.reload()
