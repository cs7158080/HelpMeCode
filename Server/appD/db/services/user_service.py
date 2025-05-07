class UserService:
    def __init__(self, user_model):
        self.user_model = user_model

    def create_user(self, user_data):
        return self.user_model.add_item(user_data)

    def find_user(self, user_id):
        return self.user_model.get_item(user_id)