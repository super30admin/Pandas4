'''
1. We filter the rows that contain a column like a string using df['col'].str.contains()
2. It returns a boolean array containing if each row satisfied the condition or not
'''
import pandas as pd

df = pd.DataFrame({'Name': ['Geeks', 'Peter', 'James', 'Jack', 'Lisa'],
				'Team': ['Boston', 'Boston', 'Boston', 'Chele', 'Barse'],
				'Position': ['PG', 'PG', 'UG', 'PG', 'UG'],
				'Number': [3, 4, 7, 11, 5],
				'Age': [33, 25, 34, 35, 28],
				'Height': ['6-2', '6-4', '5-9', '6-1', '5-8'],
				'Weight': [89, 79, 113, 78, 84],
				'College': ['MIT', 'MIT', 'MIT', 'Stanford', 'Stanford'],
				'Salary': [99999, 99994, 89999, 78889, 87779]},
				index =['ind1', 'ind2', 'ind3', 'ind4', 'ind5'])
print(df, "\n")

#1:  Filter all rows where position contains PG
df1 = df[df['Position'].str.contains("PG")]
print(df1)

 #2: Filter all rows where either Team contains ‘Boston’ or College contains ‘MIT’
df2 = df[df['Team'].str.contains("Boston") | df['Team'].str.contains("MIT")]
print(df2)

#3: Filter rows checking Team name contains ‘Boston and Position must be PG
df3 = df[df['Team'].str.contains('Boston') & df['Position'].str.contains("PG")]
print(df3)

#4: Filter rows checking Position contains PG and College must contains like MIT
df4 = df[df['Position'].str.contains("PG") & df['College'].str.contains("MIT")]
print(df4)
