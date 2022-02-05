
  
import unittest
from app.models import Comment


class TestComment(unittest.TestCase):
    def setUp(self):
        self.new_comment = Comment(
            id=12345, comment='A comment', user_id='John Doe', pitch_id=123)

    def tearDown(self):
        Comment.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))