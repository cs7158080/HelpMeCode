class AnswersModel:
    def __init__(self, db):
        self.collection = db['answers']

    def add_answer(self, answer_data):
        return self.collection.insert_one(answer_data)

    def get_answer(self, answer_id):
        return self.collection.find_one({'_id': answer_id})