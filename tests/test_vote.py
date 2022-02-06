from unicodedata import name
import unittest
from app.models import Vote, User


class TestVote(unittest.TestCase):
    def setUp(self):
        self.user = User(username="james", id=1, name="James Muriithi", email="m@a.com")
        self.vote = Vote(vote=1, user=self.user, pitch_id=1)

    def test_instance(self):
        self.assertTrue(isinstance(self.vote, Vote))

    def test_vote_user(self):
        self.assertTrue(isinstance(self.vote.user, User))  
        self.assertEquals(self.vote.user.id, self.user.id)    