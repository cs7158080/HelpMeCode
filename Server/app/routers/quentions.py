from fastapi import APIRouter, Depends
from db.Modules.quentions import Quentions
from db.Services.dependencies import get_mongo_operations, get_db

router = APIRouter(tags=["quentions"])

def create_quentions_service(
    mongo_operations = Depends(lambda db=Depends(get_db): get_mongo_operations("quentions", db))
):
    """
    Factory function to create a singleton Quentions service.
    """
    if not hasattr(create_quentions_service, "_instance"):
        create_quentions_service._instance = Quentions(mongo_operations)
    return create_quentions_service._instance

def get_quentions_service(
    quentions_service=Depends(create_quentions_service)
):
    """
    Dependency to provide a Quentions service.
    """
    return quentions_service

# def get_quentions_service(
#     mongo_operations = Depends(lambda db=Depends(get_db): get_mongo_operations("quentions", db))
# ):
#     """
#     Dependency to provide a Quentions service.
#     """
#     return Quentions(mongo_operations)

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