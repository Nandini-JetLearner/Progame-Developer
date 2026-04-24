class User:
    def login(self):
        print("User Logged In")

class PremiumUser(User):
    def access_premium(self):
        print("Accessing premium features")

u= PremiumUser()
u.login()
u.access_premium()