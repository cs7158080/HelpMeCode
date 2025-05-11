from pymongo import MongoClient
import os

class MongoConnection:
    def __init__(self, uri: str = None, database_name: str = None):
        self.uri = uri or os.getenv("URI", "mongodb://host.docker.internal:27017/")
        self.database_name = database_name or os.getenv("DB_NAME", "HelpMeCode")
        self.client = None
        self.database = None

    def connect(self):
        try:
            self.client = MongoClient(self.uri)
            self.database = self.client.get_database(self.database_name)
            print(f"Connected to MongoDB database: {self.database_name}")
        except Exception as e:
            print(f"Failed to connect to MongoDB: {e}")
            raise

    # def get_database(self):
    #     if not self.database:
    #         raise Exception("Database connection is not established. Call connect() first.")
    #     return self.database

    def close(self):
        if self.client:
            self.client.close()
            print("MongoDB connection closed.")
# Export the class for external usage
mongo_connection = MongoConnection()

