from transformers import BertTokenizer

# Load the pre-trained BERT tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Student feedback sentences
feedback = [
    "The course was very interesting and informative.",
    "I did not like the teaching methods.",
    "The assignments were helpful and easy to understand.",
    "The lectures were boring and difficult."
]

# Tokenize each sentence
for sentence in feedback:
    tokens = tokenizer.tokenize(sentence)
    token_ids = tokenizer.convert_tokens_to_ids(tokens)

    print("Feedback:", sentence)
    print("Tokens:", tokens)
    print("Token IDs:", token_ids)
    print("-" * 60)