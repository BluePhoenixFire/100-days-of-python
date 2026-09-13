
class User:
    def __init__(self, user_id, username):
        self.user_id: int = user_id
        self.username: str = username
        self.followers: int = 0
        self.following: int = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User(1000, "Purry")
user_2 = User(1001,"Nippy")

user_1.follow(user_2)

print(vars(user_1))
print(vars(user_2))

