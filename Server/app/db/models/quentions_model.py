class QuestionsModel:
    def __init__(self, db):
        self.collection = db['questions']

    def add_question(self, question_data):
        return self.collection.insert_one(question_data)

    def get_question(self, question_id):
        return self.collection.find_one({'_id': question_id})
        