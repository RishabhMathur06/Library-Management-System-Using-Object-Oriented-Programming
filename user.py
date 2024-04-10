class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return f"Name: {self.name}, User ID: {self.id}"

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, user_id):
        new_user = User(name, user_id)
        self.users.append(new_user)

    def list_users(self):
        print("\n")
        print("Registered Users")
        print("----------------")
        for user in self.users:
            print(user)

    def search_user_by_name(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None
    
    def search_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
