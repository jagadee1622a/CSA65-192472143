from transformers import BertTokenizer,GPT2Tokenizer

bert = BertTokenizer.from_pretrained("bert-base-uncased")

gpt = GPT2Tokenizer.from_pretrained("gpt2")

text = "Artificial Intelligence"

print("BERT:", bert.tokenize(text))

print("GPT2:", gpt.tokenize(text))
