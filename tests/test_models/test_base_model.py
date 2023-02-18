<<<<<<< HEAD
import unittest
import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage
=======
#!/usr/bin/python3

import unittest
import uuid
from datetime import datetime, timedelta
>>>>>>> cd9d38ee7216e648933f0eda01a10010b3bfcb06
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
<<<<<<< HEAD
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
=======
        self.base_model = BaseModel()

    def test_id(self):
        self.assertIsInstance(self.base_model.id, str)
        self.assertEqual(len(self.base_model.id), 36)
        self.assertRegex(self.base_model.id, '[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}')

    def test_created_at(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_updated_at_is_updated(self):
        created_at = self.base_model.created_at
        self.base_model.save()
        self.assertNotEqual(created_at, self.base_model.updated_at)

    def test_str_representation(self):
        self.assertIsInstance(str(self.base_model), str)
        self.assertRegex(str(self.base_model), 'BaseModel\([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\).*')

    def test_init_with_kwargs(self):
        kwargs = {
            'id': str(uuid.uuid4()),
            'created_at': datetime.now(),
            'updated_at': datetime.now() + timedelta(seconds=1),
            'test_key': 'test_value'
        }
        base_model = BaseModel(**kwargs)

        self.assertEqual(base_model.id, kwargs['id'])
        self.assertEqual(base_model.created_at, kwargs['created_at'])
        self.assertEqual(base_model.updated_at, kwargs['updated_at'])
        self.assertEqual(base_model.test_key, kwargs['test_key'])

if __name__ == '__main__':
>>>>>>> cd9d38ee7216e648933f0eda01a10010b3bfcb06
    unittest.main()
