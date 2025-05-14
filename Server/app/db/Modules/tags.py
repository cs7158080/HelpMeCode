
from pydantic import BaseModel

class Tag(BaseModel):
    tagname: str


class TagService:
    def __init__(self, tags_model):
        self.tags_model=tags_model

    def getall_tags(self):
        return self.tags_model.getAllItems(sort_field="name", ascending=True)
    
    def create_tags(self, tagdata):
        return self.tags_model.add_item(tagdata)    
    
    def find_tags(self, tagsname):
        return self.tags_model.getAllItems(filter=tagsname)    
    
   