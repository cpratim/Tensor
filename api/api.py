from config import SECRET
import openai
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification, AdamW
import torch

difficulty_labels = ['easy', 'medium', 'hard']
subject_labels    = ['math', 'computer science', 'economics']

openai.api_key = SECRET

class API(object):

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        self.difficulty_model = AutoModelForSequenceClassification.from_pretrained("models/difficulty_model", num_labels=3)
        self.subject_model = AutoModelForSequenceClassification.from_pretrained("models/subject_model", num_labels=3)

    def get_question_metrics(self, question):
        token = self.tokenizer([question], padding=True, truncation=True, return_tensors="pt")
        difficulty = self.difficulty_model(**token)
        subject = self.subject_model(**token)
        difficulty = difficulty_labels[torch.argmax(difficulty.logits, dim=1).item()]
        subject = subject_labels[torch.argmax(subject.logits, dim=1).item()]
        return difficulty, subject
    

if __name__ == '__main__':
    api = API('data')
    print(api.get_question_metrics('What is the derivative of x^2?'))

