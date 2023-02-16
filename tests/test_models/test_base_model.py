import unittest
import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()

    def test_init_without_kwargs(self):
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertIn(self.model, self.storage.all().values())

    def test_init_with_kwargs(self):
        model = BaseModel(id="test", created_at="2020-05-01T00:00:00.000000", updated_at="2020-05-02T00:00:00.000000")
        self.assertIsInstance(model, BaseModel)
        self.assertEqual(model.id, "test")
        self.assertEqual(model.created_at.isoformat(), "2020-05-01T00:00:00")
        self.assertEqual(model.updated_at.isoformat(), "2020-05-02T00:00:00")

    def test_str(self):
        self.assertIsInstance(str(self.model), str)

    def test_save(self):
        original_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(original_updated_at, self.model.updated_at)

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["created_at"], self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], self.model.updated_at.isoformat())

if __name__ == "__main__":
    unittest.main()
