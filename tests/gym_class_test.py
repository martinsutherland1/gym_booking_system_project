import unittest
from models.gym_class import Gym_Class

class TestGym_class(unittest.TestCase): 
    def setUp(self):
        self.gym_class  = Gym_Class("Spin", "03/04", 09.00, 10)
    
    def test_gym_class_has_name(self):
        self.assertEqual("Spin", self.gym_class.name)

    def test_gym_class_has_time(self):
        self.assertEqual(9.00, self.gym_class.time)
    
    def test_gym_class_has_date(self):
        self.assertEqual("03/04", self.gym_class.date)
    
    def test_gym_class_has_capacity(self):
        self.assertEqual(10, self.gym_class.capacity)

    

   


