import pandas as pd
from sqlalchemy import create_engine

# Replace password with your PostgreSQL password
engine = create_engine(
   "postgresql://postgres:postgre%40123@localhost/studentdb"
)
df = pd.read_csv("../data/clean_students.csv")

df.to_sql(
    "students",
    engine,
    if_exists="replace",
    index=False
)

print("Data Loaded Successfully")