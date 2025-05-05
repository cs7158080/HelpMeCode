class PostsModel:
    def __init__(self, db):
        self.collection = db['posts']

    def add_post(self, post_data):
        return self.collection.insert_one(post_data)

    def get_post(self, post_id):
        return self.collection.find_one({'_id': post_id})