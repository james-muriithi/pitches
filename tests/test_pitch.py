import unittest
from app.models import Pitch


class TestPitch(unittest.TestCase):
    def setUp(self):
        self.new_pitch = Pitch(title="Test Post Title",
                             description="Test Content body", user_id=3)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))