from fastapi import Depends
from db.Services.MongoOperations import MongoOperations
from db.Services.MongoConnection import MongoConnection
from functools import lru_cache

@lru_cache()
def get_mongo_client():
    """
    Create and cache a MongoDB client.
    """
    mongo_client = MongoConnection()
    mongo_client.connect()
    return mongo_client

def shutdown_db_client(mongo_client = Depends(get_mongo_client)):
    """
    Close the MongoDB client when the application shuts down.
    """
    if mongo_client:
        mongo_client.close()

def get_db(mongo_client = Depends(get_mongo_client)):
    """
    Dependency to provide a MongoDB database connection.
    """
    if not mongo_client:
        raise Exception("MongoDB client is not initialized.")
    return mongo_client.get_database()

def get_mongo_operations(collection_name: str, db):
    return MongoOperations(db, collection_name)