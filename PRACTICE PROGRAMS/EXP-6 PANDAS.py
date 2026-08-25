import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [21, 22, 20],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)

print(df)
