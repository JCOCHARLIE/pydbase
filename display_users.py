from main import User

myusers = User.select()
for user in myusers:
    print(user.name, user.email, user.password)