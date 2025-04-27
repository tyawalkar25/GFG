class UserDB:
    def __init__(self):
        self.users = []

    def insert(self,user):
        i = 0
        while i < len(self.users):
            if (self.users[i].username > user.username):
                break
            i += 1
        self.users.insert(i,user)

    def find(self,username):
        for user in self.users:
            if user.username == username:
                return user
    

    def update(self,username):
        pass

    def list_all(self):
        return self.users