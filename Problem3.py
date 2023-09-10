# How to get column names in Pandas dataframe

import pandas as pd
df=pd.DataFrame({'Name': ['Geeks', 'Peter', 'James', 'Jack', 'Lisa'],
                   'Team': ['Boston', 'Boston', 'Boston', 'Chele', 'Barse'],
                   'Position': ['PG', 'PG', 'UG', 'PG', 'UG'],
                   'Number': [3, 4, 7, 11, 5],
                   'Age': [33, 25, 34, 35, 28],
                   'Height': ['6-2', '6-4', '5-9', '6-1', '5-8'],
                   'Weight': [89, 79, 113, 78, 84],
                   'College': ['MIT', 'MIT', 'MIT', 'Stanford', 'Stanford'],
                   'Salary': [99999, 99994, 89999, 78889, 87779]},
                   index =['ind1', 'ind2', 'ind3', 'ind4', 'ind5'])


print(df.columns)
for col in df.columns:
    print(col)

print(list(df.columns))
print(df.columns.values.tolist())
print(df.keys())