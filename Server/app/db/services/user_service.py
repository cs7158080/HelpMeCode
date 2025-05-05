class UserService:
    def __init__(self, user_model):
        self.user_model = user_model

    def create_user(self, name, email):
        user_data = {"name": name, "email": email}
        return self.user_model.add_user(user_data)

    def find_user(self, user_id):
        return self.user_model.get_user(user_id)