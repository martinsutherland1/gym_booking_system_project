import pdb

from models.member import Member
from models.session import Session
from models.gym_class import Gym_Class

import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.session_repository as session_repository

session_repository.delete_all()
member_repository.delete_all()
gym_class_repository.delete_all()







pdb.set_trace()
