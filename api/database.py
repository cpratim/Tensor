import json
import os
from api import API
from random import randint
from pprint import pprint

api = API()

class Database(object):
    
    def __init__(self, path):
        self.database = {}
        self.path = path

        tables = os.listdir(f'{path}/tables')
        for table in tables:
            if not table.endswith('.json'):
                continue
            with open(f'{path}/tables/{table}', 'r') as f:
                self.database[table.split('.')[0]] = json.load(f)
        
    def add_question(self, body, answer):

        idx = str(abs(hash(body)))
        while idx in self.database['questions']:
            idx = str(abs(hash(idx)))

        difficulty, subject = api.get_question_metrics(body)
        self.database['questions'][idx] = {
            'question': body,
            'answer': answer,
            'difficulty': difficulty,
            'subject': subject,
            'likes': 0
        }
        self.save()

    def get_size(self, length):
        if length < 10:
            return 'short'
        elif length < 20:
            return 'medium'
        return 'long'

    def query(self, query_json):
        results = []
        length_range = query_json['length_range']
        difficulties = query_json['difficulty_range']
        subjects     = query_json['subjects']
        for idx in self.database['questions']:
            question = self.database['questions'][idx]
            size = self.get_size(len(question['question'].split()))
            if size in length_range and question['difficulty'] in difficulties and question['subject'] in subjects:
                results.append((idx, question['likes'], question['question'], question['answer'], question['difficulty'], question['subject']))

        results.sort(key=lambda x: x[1], reverse=True)
        return results

    def upload_image(self, image):
        idx = str(abs(hash(image)))
        while idx in self.database['images']:
            idx = str(abs(hash(idx)))

        self.database['images'][idx] = image
        with open(f'{self.path}/images/{idx}.jpg', 'wb') as f:
            f.write(image)
        self.save()

    def save(self):
        for table in self.database:
            with open(f'{self.path}/tables/{table}.json', 'w') as f:
                json.dump(self.database[table.split('.')[0]], f, indent=4)
                

if __name__ == '__main__':
    db = Database('database')

    query = {
        'length_range': ['short', 'medium', 'long'],
        'difficulty_range': ['easy', 'medium', 'hard'],
        'subjects': ['computer science']
    }
    results = db.query(query)
    with open('sample_query.json', 'w') as f:
        json.dump(results, f, indent=4)


