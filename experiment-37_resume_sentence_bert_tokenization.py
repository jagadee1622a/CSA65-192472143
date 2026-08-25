"""Resume Sentence BERT Tokenization\nTokenize an engineering-related resume sentence.\n"""

from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
sentence = "Artificial intelligence helps engineers analyze complex technical systems."
tokens = tokenizer.tokenize(sentence)
token_ids = tokenizer.convert_tokens_to_ids(tokens)

print("Sentence:", sentence)
print("Tokens:", tokens)
print("Token IDs:", token_ids)
