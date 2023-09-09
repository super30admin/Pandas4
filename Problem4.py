'''
1. Renaming columns of a dataframe 
2. Using rename(), set_axis(), add_prefix & add_suffix, assign new list, str.replace on df.columns
'''

import pandas as pd

rankings = {'test': ['India', 'South Africa', 'England',
							'New Zealand', 'Australia'],
			'odi': ['England', 'India', 'New Zealand',
							'South Africa', 'Pakistan'],
			't20': ['Pakistan', 'India', 'Australia',
							'England', 'New Zealand']}

rankings_pd = pd.DataFrame(rankings)

print("Before renaming the columns")
print(rankings_pd)

# 1. Using rename function
print("Renaming one column")
df = rankings_pd.rename(columns = {'test':'TEST'})
print("\nAfter modifying first column:\n", df.columns)

print("Renaming multiple columns")
print(rankings_pd.columns)
df = rankings_pd.rename(columns = {'test':'TEST', 'odi':'ODI',
                              't20':'T20'})
print(df.columns)

# 2. By assigning a list of new column names 

df = rankings_pd
df.columns = ['TEST', 'ODI', 'T-20']
print(df)

# 3. Using set_axis method
df = df.set_axis(['A', 'B', 'C'], axis='columns')
print(df)

# 4. Using add_prefix() and add_suffix() methods - Appends prefix at beginning and suffix at the end to all columns
df = df.add_prefix('col_')
df = df.add_suffix('_1')
print(df)

# 5. Replacing part of column name using str.replace
df.columns = rankings_pd.columns.str.replace('test', 'Col_TEST')
df.columns = rankings_pd.columns.str.replace('odi', 'Col_ODI')
df.columns = rankings_pd.columns.str.replace('t20', 'Col_T20')

print(df)
