'''
1. Finding unique entries in a dataframe using uniques
2. Get number of uniques using nunique
'''
import pandas as pd

data = {
	'A':['A1', 'A2', 'A3', 'A4', 'A5'],
	'B':['B1', 'B2', 'B3', 'B4', 'B4'],
	'C':['C1', 'C2', 'C3', 'C3', 'C3'],
	'D':['D1', 'D2', 'D2', 'D2', 'D2'],
	'E':['E1', 'E1', 'E1', 'E1', 'E1'] }

df = pd.DataFrame(data)
# Unique values of column B using unique()
print(df['B'].unique())

# Number of uniques in column E using nunique()
print(df['E'].nunique(dropna = True))


