#!/usr/bin/python3

import unittest
import uuid
from datetime import datetime, timedelta
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
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
    unittest.main()
