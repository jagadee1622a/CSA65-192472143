import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Marks": [70, 85, 95]
}

df = pd.DataFrame(data)

print("Average Marks:", df["Marks"].mean())
print("Maximum Marks:", df["Marks"].max())
