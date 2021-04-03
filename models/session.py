class Session:
    def __init__(self, member, gym_class, id = None):
        self.member = member
        self.gym_class = gym_class
        self.id = id
        self.members = []

    def session_count(self):
        return len(self.members)
    
    def add_to_session(self, session):
        self.members.append(session)




