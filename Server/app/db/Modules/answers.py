from pydantic import BaseModel

class Content(BaseModel):
    context: str
    userName: str

class Answer(BaseModel):
    Date: str
    Context: str
    Tags: list[int]
    UserName: str
    Content: list[Content]
    QuentionId : str
    

class AnswerModel:
    def __init__(self, answer_model):
        self.answer_model = answer_model

    def create_answer(self, answer_data):
        result = self.answer_model.add_item(answer_data.dict())
        return {"inserted_id": str(result.inserted_id)} if result else {"message": "Insertion failed"}
    
    def get_answers_by_quention_id(self, quentionId : str):
        filter = {'QuentionId': quentionId}
        response = self.answer_model.getAllItems(filter=filter)
        if response:
            response = [{**item, "_id": str(item["_id"])} for item in response]
            return response
        else:
            return {"message : response is not found"}
        