import pandas as pd

data = {
    "Name": ["Ram", "Sam"],
    "Marks": [80, 90]
}

df = pd.DataFrame(data)

df["Result"] = ["Pass", "Pass"]

print(df)
