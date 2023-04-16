from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification, AdamW
import torch.nn as nn
import torch
import json
import os
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from warnings import filterwarnings

filterwarnings('ignore')

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

def load_dataset(label):
    dataset = []
    for file in os.listdir('data'):
        if not file.endswith('.json'):
            continue
        with open(f'data/{file}', 'r') as f:
            data = json.load(f)
        
        for q in data:
            dataset.append(
                {
                    'text': q['question'],
                    'label': q[label].lower()
                }
            )
    return dataset

if __name__ == '__main__':
    dataset = load_dataset('difficulty')
    label_values = {'easy': 0, 'medium': 1, 'hard': 2}
    output_values = {0: 'easy', 1: 'medium', 2: 'hard'}
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=3)

    optimizer = AdamW(model.parameters(), lr=5e-5)
    loss_fn = nn.CrossEntropyLoss()

    train_set, test_set = train_test_split(dataset, test_size=0.2)

    train_inputs = tokenizer([example["text"] for example in train_set], padding=True, truncation=True, return_tensors="pt")
    labels = torch.tensor([label_values[example["label"]] for example in train_set]) 

    model.train()
    for epoch in range(10):
        optimizer.zero_grad()
        outputs = model(**train_inputs, labels=labels)
        loss = loss_fn(outputs.logits, labels)
        loss.backward()
        optimizer.step()
        print("Epoch:", epoch, "Loss:", loss.item())

    print()
    for example in test_set:
        inputs = tokenizer([example["text"]], padding=True, truncation=True, return_tensors="pt")
        outputs = model(**inputs)
        pred = torch.argmax(outputs.logits, dim=1)
        print('Question:', example['text'])
        print('Predicted label:', output_values[pred.item()])
        print()

    model.save_pretrained("models/difficulty_model")





