class Authentication:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

# Example usage:
if __name__ == "__main__":
    user = "example_user"
    password = "example_password"
    
    auth = Authentication(user, password)
    print(f"User: {auth.get_user()}")
    print(f"Password: {auth.get_password()}")
