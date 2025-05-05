class UserModel:
    def __init__(self, db):
        self.collection = db['users']

    def add_user(self, user_data):
        return self.collection.insert_one(user_data)

    def get_user(self, user_id):
        return self.collection.find_one({'_id': user_id})