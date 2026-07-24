from transformers import pipeline

pipe = pipeline("sentiment-analysis")

print(pipe("The movie was excellent."))
