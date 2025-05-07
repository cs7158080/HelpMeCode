class GenericModel:
    def __init__(self, db, collection_name):
        self.collection = db[collection_name]
        self.db = db

    def setCollection(self, collection_name):
        self.collection = self.db[collection_name]   

    def getAllItems(self):
        return list(self.collection.find())     

    def add_item(self, item_data):
        return self.collection.insert_one(item_data)

    def get_item(self, item_id):
        return self.collection.find_one({'_id': item_id})
        