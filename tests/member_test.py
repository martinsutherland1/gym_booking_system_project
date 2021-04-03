import unittest
from models.member import Member

class TestMember(unittest.TestCase):

    def setUp(self):
        self.member = Member("Martin Sutherland", 30)

    def test_member_has_name(self):
        self.assertEqual("Martin Sutherland", self.member.name)
    
    def test_member_has_age(self):
        self.assertEqual(30, self.member.age)