from fastapi import APIRouter, Depends
from db.Services.dependencies import get_mongo_operations, get_db
from functools import lru_cache
from db.Modules.answers import AnswerModel, Answer

router = APIRouter(tags=["answers"])


@lru_cache()
def get_answers_service(
    mongo_operations=Depends(lambda db=Depends(get_db): get_mongo_operations("answers", db))
):
    """
    Dependency to provide a answers service with caching.
    """
    return AnswerModel(mongo_operations)

@router.post("/createAnswer")
def create_post(Post_data: Answer, answers_service=Depends(get_answers_service)):
    return answers_service.create_answer(Post_data)

@router.get("/getAnswersByQuentionId/{question_id}")
def get_answers_by_quention_id(question_id: str, answers_service=Depends(get_answers_service)):
    return answers_service.get_answers_by_quention_id(question_id)