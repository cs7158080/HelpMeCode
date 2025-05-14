from fastapi import APIRouter,Depends
from db.Services.dependencies import get_db, get_mongo_operations
router = APIRouter(tags=["tags"]) 
from db.Modules.tags import Tag, TagService
from functools  import lru_cache

@lru_cache()
def get_tags_service(
    mongo_operations=Depends(lambda db=Depends(get_db): get_mongo_operations("tags", db))
):
    """
    Dependency to provide a Quentions service with caching.
    """
    return TagService(mongo_operations)


@router.get("/getalltags")
def read_all(tags_service=Depends(get_tags_service)):
   return tags_service.getall_tags()

@router.get("/get-tags-by-name/{tagname}")
def read_tags(tagname:str,tags_service=Depends(get_tags_service)):
 return tags_service.find_tags(tagname)
   
@router.post("/create-tags")
def create(tag:Tag,tags_service=Depends(get_tags_service)):
    return tags_service.create_tags(tag)
