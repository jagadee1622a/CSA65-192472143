import pandas as pd

data = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [65, 92, 78, 88]
}

df = pd.DataFrame(data)

print(df[df["Marks"] > 80])
