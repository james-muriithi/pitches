import unittest
from app.models import Category


class TestCategory(unittest.TestCase):
    def setUp(self):
        self.category = Category(name="Test Category")

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))