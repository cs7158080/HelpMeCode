from fastapi import APIRouter
router = APIRouter(tags=["tags"]) 
from db.Services.MongoConnection import MongoConnection 
from db.Services.MongoOperations import MongoOperations  
from db.Modules.tags import Tag, TagService
connectToMongo = MongoConnection()
connectToMongo.connect()
@router.get("/getalltags")
def read_all():
    if not connectToMongo.client:
        return {"error": "Failed to connect to the database."}
    
    tags_model = MongoOperations(connectToMongo.database, 'tags')
    tags_service = TagService(tags_model)
    tags_data = tags_service.getall_tags()
    if tags_data:
        tags_data = [{**tag, "_id": str(tag["_id"])} for tag in tags_data]
        return {"tags": tags_data}
    else:
        return {"message:tags is not found"}
@router.get("/get-tags-by-name/{tagname}")
def read_tags(tagname:str):
    if not connectToMongo.client:
        return {"error": "Failed to connect to the database."}
    
    tags_model = MongoOperations(connectToMongo.database, 'tags')
    tags_service = TagService(tags_model)
    tags_data = tags_service.find_tags({"tagname": tagname})
    if tags_data:
        tag = {**tags_data[0], "_id": str(tags_data[0]["_id"])} if isinstance(tags_data, list) and tags_data else None
        return {"tag": tag}
    else:
        return {"message": f"tags {tagname} not found."}
@router.post("/create-tags")
def create(tag:Tag):
    if not connectToMongo.client:
        return {"error": "Failed to connect to the database."}
    
    tags_model = MongoOperations(connectToMongo.database, 'tags')
    tags_service = TagService(tags_model)
    tags_data = tags_service.create_tags(tag.dict()) 
    if tags_data:
        return {"message": f"Tag {tag.tagname} created successfully."}
    else:
        return {"message": "Failed to create tag."}