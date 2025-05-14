from fastapi import Depends
from db.Services.MongoOperations import MongoOperations
from db.Services.MongoConnection import MongoConnection

mongo_client = None

def startup_db_client():
    """
    Create a MongoDB client when the application starts.
    """
    global mongo_client
    mongo_client = MongoConnection()
    mongo_client.connect()
    print("MongoDB client connected.")

def shutdown_db_client():
    """
    Close the MongoDB client when the application shuts down.
    """
    global mongo_client
    if mongo_client:
        mongo_client.close()
        print("MongoDB client disconnected.")

def get_db():
    """
    Dependency to provide a MongoDB database connection.
    """
    global mongo_client
    if not mongo_client:
        raise Exception("MongoDB client is not initialized.")
    return mongo_client.get_database()

def get_mongo_operations(collection_name: str, db):
    """
    Dependency to provide a MongoOperations instance for a specific collection.
    """
    return MongoOperations(db, collection_name)