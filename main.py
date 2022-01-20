import pandas as pd


# reading the database
data = pd.read_csv("C:\Users\Lenovo\OneDrive\Desktop\corona1.csv")

# printing the top 10 rows
display(data.head(10))
