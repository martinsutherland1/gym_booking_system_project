import pdb

from models.member import Member
from models.session import Session

import repositories.member_repository as member_repository

member1 = Member("Martin Sutherland", 31)
member_repository.save(member1)

pdb.set_trace()
