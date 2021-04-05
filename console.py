import pdb

from models.member import Member
from models.session import Session
from models.gym_class import Gym_Class

import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.session_repository as session_repository

member_repository.delete_all()
gym_class_repository.delete_all()
session_repository.delete_all()

member1 = Member("Martin Sutherland", 31)
member_repository.save(member1)
member2 = Member("Katelyn Hayes", 24)
member_repository.save(member2)

gym_class1 = Gym_Class("Spin", "03/04", "09.00", 16)
gym_class_repository.save(gym_class1)
gym_class2 = Gym_Class("Dance", "03/04", "09.30", 10)
gym_class_repository.save(gym_class2)

# session1 = Session(member1, gym_class1)
# session_repository.save(session1)
# session2 = Session(member2, gym_class2)
# session_repository.save(session2)




pdb.set_trace()
