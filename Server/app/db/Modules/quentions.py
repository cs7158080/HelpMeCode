from pydantic import BaseModel

class Quention(BaseModel):
    Date: str
    Context: str
    Tags: list[int]
    UserId: str

class QuentionModel:
    def __init__(self, quention_model):
        self.quention_model = quention_model

    def get_all_quentions(self):
        response = self.quention_model.getAllItems()  
        if response:
            response = [{**item, "_id": str(item["_id"])} for item in response]
            return response
        else:
            return {"message : response is not found"}

    def create_quention(self, quention_data):
        result = self.quention_model.add_item(quention_data.dict())
        return {"inserted_id": str(result.inserted_id)} if result else {"message": "Insertion failed"}

    def get_last_quention(self):
        response = self.get_all_quentions()
        if response:
            response = sorted(response, key=lambda x: x['_id'], reverse=True)
            quention = response[:1]
            return quention[0] if quention else None
        else:
            return None
    
    def get_quentions_by_tags(self, tags):
        filter = {'Tags': {'$in': tags}}
        pipeline = [
            {'$match': filter},
            {'$project': {
            'Tags': 1,
            'match_count': {'$size': {'$setIntersection': ['$Tags', tags]}}
            }},
            {'$sort': {'match_count': -1}}
        ]
        response = list(self.quention_model.aggregate(pipeline))
        if response:
            response = [{**item, "_id": str(item["_id"])} for item in response]
            return response
        else:
            return {"message": "Response not found"}
