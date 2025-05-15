from pydantic import BaseModel

class Content(BaseModel):
    context: str
    userName: str

class Post(BaseModel):
    Date: str
    label: str
    Context: str
    Tags: list[int]
    UserId: str
    Content: list[Content]
    

class PostModel:
    def __init__(self, post_model):
        self.post_model = post_model

    def get_all_posts(self):
        response = self.post_model.getAllItems()  
        if response:
            response = [{**item, "_id": str(item["_id"])} for item in response]
            return response
        else:
            return {"message : response is not found"}

    def create_post(self, post_data):
        result = self.post_model.add_item(post_data.dict())
        return {"inserted_id": str(result.inserted_id)} if result else {"message": "Insertion failed"}

    def get_last_post(self):
        response = self.get_all_posts()
        if response:
            response = sorted(response, key=lambda x: x['_id'], reverse=True)
            post = response[:1]
            return post[0] if post else None
        else:
            return None
    
    def get_posts_by_tags(self, tags):
        filter = {'Tags': {'$in': tags}}
        pipeline = [
            {'$match': filter},
            {'$addFields': {
                'match_count': {'$size': {'$setIntersection': ['$Tags', tags]}}
            }},
            {'$sort': {'match_count': -1}}
        ]
        response = list(self.post_model.aggregate(pipeline))
        if response:
            response = [{**item, "_id": str(item["_id"])} for item in response]
            return response
        else:
            return {"message": "Response not found"}
