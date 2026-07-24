from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

sentence = "Natural Language Processing"

tokens = tokenizer.tokenize(sentence)

ids = tokenizer.convert_tokens_to_ids(tokens)

print("Tokens:", tokens)

print("IDs:", ids)
