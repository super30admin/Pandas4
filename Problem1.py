#  Problem 1 : Get all rows in a Pandas DataFrame containing given substring
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
print(df)

# Code #1: Check the values PG in column Position
print(df[df['Position'].str.contains('PG')])

# Code #2: Filter all rows where either Team contains ‘Boston’ or College contains ‘MIT’.
print(df[(df['Team'].str.contains('Boston'))|(df['College'].str.contains('MIT'))])

# Code #3: Filter rows checking Team name contains ‘Boston and Position must be PG.
print(df[df['Team'].str.contains('Boston') & df['Position'].str.contains('PG')])

# Code #4: Filter rows checking Position contains PG and College must contains like UC.
print(df[(df['Position'].str.contains('PG'))&(df['College'].str.contains('Stanford'))])