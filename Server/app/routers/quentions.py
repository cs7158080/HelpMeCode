from fastapi import APIRouter, Depends
from db.Modules.quentions import Quentions
from db.Services.dependencies import get_mongo_operations, get_db
from functools import lru_cache

router = APIRouter(tags=["quentions"])


@lru_cache()
def get_quentions_service(
    mongo_operations=Depends(lambda db=Depends(get_db): get_mongo_operations("quentions", db))
):
    """
    Dependency to provide a Quentions service with caching.
    """
    return Quentions(mongo_operations)

@router.post("/createQuention")
def create_quention(quention_data: dict, quentions_service=Depends(get_quentions_service)):
    return quentions_service.create_quention(quention_data)

@router.get("/getAllQuentions")
def get_all_quentions(quentions_service=Depends(get_quentions_service)):
    return quentions_service.get_all_quentions()

@router.get("/getLastQuention")
def get_last_quention(quentions_service=Depends(get_quentions_service)):
    return quentions_service.get_last_quention()

@router.get("/getQuentionsByTags")
def get_quentions_by_tags(tags: str, quentions_service=Depends(get_quentions_service)):
    tags_list = [int(tag) for tag in tags.split(",")]
    return quentions_service.get_quentions_by_tags(tags_list)