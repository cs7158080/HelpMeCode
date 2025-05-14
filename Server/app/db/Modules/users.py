from pydantic import BaseModel ,EmailStr
from typing import List
from db.Modules.tags import Tag

class UserTag(BaseModel):
    tag: Tag    
    canhelp: bool 



class User(BaseModel):
    name: str
    email: EmailStr 
    tags: List[UserTag] 



class UserService:
    def __init__(self, user_model):
        self.user_model = user_model

    def objectid_to_string(self, users):
        for user in users:
            user['_id'] = str(user['_id'])
        return users

    def create_user(self, user_data):
        user_dict = user_data.dict()
        result = self.user_model.add_item(user_dict)
        return str(result.inserted_id)

    def get_all_users(self):
        users = self.user_model.getAllItems()
        return self.objectid_to_string(users)

    def get_user_by_name(self, username):
        users = self.user_model.getAllItems(filter={"name": username})
        if users:
            user = users[0]
            user['_id'] = str(user['_id'])
            return user
        return None


    def get_users_by_tag(self, tag_name: str):
        filter = {"tags.tag.tagname": tag_name}
        users = self.user_model.getAllItems(filter=filter)
        return self.objectid_to_string(users)

    def get_users_by_tag_value_true(self, tag_name: str):
        filter = {"tags": {"$elemMatch": {"tag.tagname": tag_name, "canhelp": True}}}  
        users = self.user_model.getAllItems(filter=filter)
        return self.objectid_to_string(users)

    def get_users_by_tag_value_false(self, tag_name: str):
        filter = {"tags": {"$elemMatch": {"tag.tagname": tag_name, "canhelp": False}}} 
        users = self.user_model.getAllItems(filter=filter)
        return self.objectid_to_string(users)
