class MongoOperations:
    """
    A class to perform basic operations on a MongoDB collection.
    """
    def __init__(self, db, collection_name):
        self.db = db
        self.collection = db.get_collection(collection_name)

    def setCollection(self, collection_name):
        self.collection = self.db.get_collection(collection_name)   

    def getAllItems(self):
        return list(self.collection.find())     

    def add_item(self, item_data):
        return self.collection.insert_one(item_data)

    def get_item(self, item_id):
        return self.collection.find_one({'_id': item_id})
        