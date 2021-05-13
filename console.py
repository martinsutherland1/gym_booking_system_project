import pdb

from models.member import Member
from models.session import Session
from models.gym_class import Gym_Class
from models.membership_type import Membership_type

import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.session_repository as session_repository
import repositories.membership_type_repository as membership_type_repository

# session_repository.delete_all()
# membership_type_repository.delete_all()
# member_repository.delete_all()
# gym_class_repository.delete_all()

# mem1 = Membership_type("Premier")
# mem2 = Membership_type("Standard")
# membership_type_repository.save(mem1)
# membership_type_repository.save(mem2)

# # member1 = Member("Rachel Green", 28, 11)
# member2 = Member("Chandler Bing", 30, 14)
# # member_repository.save(member1)
# member_repository.save(member2)

class1 = Gym_Class("Spin", "21/06/21", "10:00", 4, "Standard")
gym_class_repository.save(class1)
class2 = Gym_Class("Spin", "21/06/21", "10:00", 4, "Standard")
class3 = Gym_Class("Spin", "21/06/21", "10:00", 4, "Standard")
class4 = Gym_Class("Spin", "21/06/21", "10:00", 4, "Standard")
class5 = Gym_Class("Spin", "21/06/21", "10:00", 4, "Standard")
class6 = Gym_Class("Spin", "21/06/21", "10:00", 4, "Standard")
class7 = Gym_Class("Spin", "21/06/21", "10:00", 4, "Standard")
class8 = Gym_Class("Spin", "21/06/21", "10:00", 4, "Standard")
gym_class_repository.save(class2)
gym_class_repository.save(class3)
gym_class_repository.save(class4)
gym_class_repository.save(class5)
gym_class_repository.save(class6)
gym_class_repository.save(class7)
gym_class_repository.save(class8)










pdb.set_trace()
