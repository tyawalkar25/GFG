class User:
    def __init__(self,username,name,email):
        self.username = username
        self.name = name
        self.email = email
        print("User created")

user1 = User('tyawalkar3','tapan','tyawalkar3@gmail.com')
print(user1.name)