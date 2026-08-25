from transformers import GPT2Tokenizer,GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

model = GPT2LMHeadModel.from_pretrained("gpt2")

input_ids = tokenizer.encode("Deep learning is", return_tensors="pt")

output = model.generate(input_ids,max_length=40)

print(tokenizer.decode(output[0]))
