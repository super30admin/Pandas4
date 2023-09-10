# Problem 5 : Get unique values from a column in Pandas DataFrame

import pandas as pd


data = {
	'A':['A1', 'A2', 'A3', 'A4', 'A5'],
	'B':['B1', 'B2', 'B3', 'B4', 'B4'],
	'C':['C1', 'C2', 'C3', 'C3', 'C3'],
	'D':['D1', 'D2', 'D2', 'D2', 'D2'],
	'E':['E1', 'E1', 'E1', 'E1', 'E1'] }


df = pd.DataFrame(data)

# Get the unique values of 'B' column
print(df.B.unique())

# : Get number of unique values in a column
print(df.C.nunique())

