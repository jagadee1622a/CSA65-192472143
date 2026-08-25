"""BERT vs GPT 2 Tokenization\nCompare tokenization of the same engineering sentence.\n"""

from transformers import BertTokenizer, GPT2Tokenizer

sentence = "Artificial intelligence improves engineering design and analysis."

bert = BertTokenizer.from_pretrained("bert-base-uncased")
gpt2 = GPT2Tokenizer.from_pretrained("gpt2")

print("Sentence:", sentence)
print("\nBERT tokens:", bert.tokenize(sentence))
print("BERT IDs:", bert.convert_tokens_to_ids(bert.tokenize(sentence)))
print("\nGPT-2 tokens:", gpt2.tokenize(sentence))
print("GPT-2 IDs:", gpt2.convert_tokens_to_ids(gpt2.tokenize(sentence)))
