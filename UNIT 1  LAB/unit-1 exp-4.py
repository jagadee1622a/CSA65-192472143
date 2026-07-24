import pandas as pd

data = {
    "Name":["Alice","Bob","Charlie","David"],
    "Grade":["A","B","A","C"]
}

df = pd.DataFrame(data)

print(df)
import numpy
import pandas
import matplotlib
import sklearn
import torch
import transformers

print("NumPy:", numpy.__version__)
print("Pandas:", pandas.__version__)
print("Matplotlib:", matplotlib.__version__)
print("Scikit-learn:", sklearn.__version__)
print("PyTorch:", torch.__version__)
print("Transformers:", transformers.__version__)
