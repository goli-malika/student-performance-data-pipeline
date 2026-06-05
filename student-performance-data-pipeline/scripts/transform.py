import pandas as pd

df = pd.read_csv("../data/students.csv")

# Create Average column
df["Average"] = (
    df["Math"] +
    df["Science"] +
    df["English"]
) / 3

# Performance Category
df["Performance"] = df["Average"].apply(
    lambda x: "Excellent" if x >= 90
    else "Good" if x >= 75
    else "Needs Improvement"
)

print(df)

df.to_csv("../data/clean_students.csv", index=False)

print("Transformation Completed")