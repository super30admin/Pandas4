'''
We find different ways of getting columns of a dataframe.
Using head(), df.columns, df.columns.values, df.columns.values.tolist, sorted.
'''
import pandas as pd
	
data = pd.read_csv("nba.csv")
	
# 1. Using head()
data_top = data.head()
print(data_top)

# 2. Using a for loop on columns attribute
for col in data.columns:
    print(col)

# 3. Using list constructor
print(list(data.columns))

# 4. Using keys function
print(data.keys())

# 5. Using columns.values 
print(data.columns.values)

# 6. tolist on columns.values
print(data.columns.values.tolist())

# 7. Using sorted method. Returns columns in ascending order
print(sorted(data))