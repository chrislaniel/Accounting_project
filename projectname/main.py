import pandas as pd

csv_path = "/Users/christophe/Downloads/pcbanking-3.csv"

data = pd.read_csv(csv_path)
print(data.head())
