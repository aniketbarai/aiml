import pandas as pd

data = pd.read_csv("./Students_Grading_Dataset.csv")
print(data.head())

print("Missing Values: ")
print(data.isnull().sum())

print("Duplicate Values: ")
print(data.duplicated().sum())

print("Age greater then 20: ")
print(data[data["Age"] > 20])
