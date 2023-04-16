import openai 
from config import SECRET
import os
import json
from random import choice
from database import Database
from time import sleep

db = Database('database')

openai.api_key = SECRET

questions = []
for file in os.listdir('data'):
    data = json.load(open(f'data/{file}', 'r'))
    for q in data:
        body = q['question'] + '|' + q['answer']
        questions.append(body)

def generate_question(sample):
    completion = openai.ChatCompletion()
    chat_log = []
    prompt = "Make 10 questions similiar to this one with the answer after it with a | in between and the questions seperated '$' (dont number them): \n" + sample
    chat_log.append({'role': 'user', 'content': prompt})
    response = completion.create(model='gpt-3.5-turbo', messages=chat_log)
    reply = response.choices[0]['message']['content']
    generated = reply.split('$')
    for q in generated:
        q = q.strip()
        if q == '':
            continue
        try:
            question, answer = q.split('|')
            db.add_question(question, answer)
            print('Q: ', question)
            print('A: ', answer)
            print('-----------------')
        except:
            print('Error: ', q)

def generate_N(N):
    for i in range(N):
        sample = choice(questions)
        gen = generate_question(sample)
        sleep(20)
        print(f'{i} | {gen}')

if __name__ == '__main__':
    sample = choice(questions)
    generate_N(20)