import pandas as pd

csv_path = "/Users/christophe/Downloads/pcbanking-3.csv"

data = pd.read_csv(csv_path)
print(data.head())


# Python program to execute
# main directly
print ("Always executed")
 
if __name__ == "__main__":
    print ("Executed when invoked directly")
else:
    print ("Executed when imported")
