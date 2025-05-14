
from pydantic import BaseModel

class Tag(BaseModel):
    tagname: str


class TagService:
    def __init__(self, tags_model):
      self.tags_model=tags_model
     
    def getall_tags(self):
        response= self.tags_model.getAllItems(sort_field="name", ascending=True)
        if response:
         response = [{**tag, "_id": str(tag["_id"])} for tag in response]
         return {"tags": response}
        else:
         return {"message:tags is not found"}
    
    def create_tags(self, tagdata):

        tagdict = tagdata.dict()
        response= self.tags_model.add_item(tagdict) 
        if response:
         return {"message": f"Tag {tagdata.tagname} created successfully."}
        else:
         return {"message": "Failed to create tag."}   
    
    def find_tags(self, tagsname):
        response= self.tags_model.getAllItems(filter={"tagname":tagsname})    
        if response:
         response = {**response[0], "_id": str(response[0]["_id"])} if isinstance(response, list) and response else None
         return {"tag": response}
        else:
         return {"message:tags is not found"}
   