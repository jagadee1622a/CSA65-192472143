from transformers import BertTokenizer,BertModel
import torch

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

model = BertModel.from_pretrained("bert-base-uncased")

texts = [
    "AI is transforming the world.",
    "Artificial Intelligence is changing the world."
]

for text in texts:
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    print(text)
    print(outputs.last_hidden_state.mean(dim=1))
