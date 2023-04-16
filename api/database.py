import json
import os
from api import API

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

    def add_like(self, idx):
        self.database['questions'][idx]['likes'] += 1
        self.save()

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
    db.add_question('What is the derivative of x^2?', '2x')