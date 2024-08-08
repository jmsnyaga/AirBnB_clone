import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Set up a new BaseModel instance for testing."""
        self.model = BaseModel()

    def test_initialization(self):
        """Test initialization of BaseModel."""
        self.assertIsInstance(self.model, BaseModel)
        self.assertTrue(isinstance(self.model.id, str))
        self.assertTrue(isinstance(self.model.created_at, datetime))
        self.assertTrue(isinstance(self.model.updated_at, datetime))

    def test_save(self):
        """Test the save method."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method."""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertTrue(isinstance(model_dict["created_at"], str))
        self.assertTrue(isinstance(model_dict["updated_at"], str))

    def test_update(self):
        """Test updating attributes."""
        self.model.update(name="John Doe")
        self.assertEqual(self.model.name, "John Doe")


if __name__ == "__main__":
    unittest.main()
