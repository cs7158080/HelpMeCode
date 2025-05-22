from fastapi import APIRouter, Depends
from db.Services.dependencies import get_mongo_operations, get_db
from functools import lru_cache
from db.Modules.posts import PostModel, Post

router = APIRouter(tags=["posts"])


@lru_cache()
def get_posts_service(
    mongo_operations=Depends(lambda db=Depends(get_db): get_mongo_operations("posts", db))
):
    """
    Dependency to provide a posts service with caching.
    """
    return PostModel(mongo_operations)

@router.post("/createPost")
def create_post(Post_data: Post, posts_service=Depends(get_posts_service)):
    return posts_service.create_post(Post_data)

@router.get("/getAllposts")
def get_all_posts(posts_service=Depends(get_posts_service)):
    return posts_service.get_all_posts()

@router.get("/getLastPost")
def get_last_post(posts_service=Depends(get_posts_service)):
    return posts_service.get_last_post()

@router.get("/getPostsByTags/{tags}")
def get_posts_by_tags(tags: str, posts_service=Depends(get_posts_service)):
    tags_list = [int(tag) for tag in tags.split(",")]
    return posts_service.get_posts_by_tags(tags_list)