import unittest
from models.session import Session
from models.gym_class import Gym_Class
from models.member import Member

class TestSession(unittest.TestCase):

    def setUp(self):
        member1 = Member("Martin Sutherland", 30, "Premier")
        gym_class1  = Gym_Class("Spin", "03/04", 09.00, 10, "Premier")
        self.session = Session(member1, gym_class1)
        

    def test_session_has_gym_class(self):
        self.assertEqual("Spin", self.session.gym_class.name)
        
        

    def test_session_has_member(self):
        self.assertEqual("Martin Sutherland", self.session.member.name)
    
    def test_can_add_guest_class(self):
        member1 = Member("Martin Sutherland", 30, "Premier")
        gym_class1  = Gym_Class("Spin", "03/04", 09.00, 10, "Premier")
        self.session = Session(member1, gym_class1)
        self.session.add_to_session(self.session)
        
        self.assertEqual(1, self.session.session_count())
