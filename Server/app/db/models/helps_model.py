class HelpsModel:
    def __init__(self, db):
        self.collection = db['helps']

    def add_help(self, help_data):
        return self.collection.insert_one(help_data)

    def get_help(self, help_id):
        return self.collection.find_one({'_id': help_id})