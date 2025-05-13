class MongoOperations:
    """
    A class to perform basic operations on a MongoDB collection.
    """
    def __init__(self, db, collection_name):
        self.db = db
        self.collection = db.get_collection(collection_name)

    def setCollection(self, collection_name):
        self.collection = self.db.get_collection(collection_name)   

    def getAllItems(self, sort_field=None, ascending=True, filter=None):
      sort_order = 1 if ascending else -1
      if filter is None:
        if sort_field:
         return list(self.collection.find().sort(sort_field, sort_order))
        else:
            return list(self.collection.find())  # ללא מיון
      else:
       if sort_field:
         return list(self.collection.find(filter).sort(sort_field, sort_order))
       else:
         return list(self.collection.find(filter)) 

    def add_item(self, item_data):
        return self.collection.insert_one(item_data)
 
