# How to rename columns in Pandas DataFrame
# Import pandas package
import pandas as pd

# Define a dictionary containing ICC rankings
rankings = {'test': ['India', 'South Africa', 'England',
							'New Zealand', 'Australia'],
			'odi': ['England', 'India', 'New Zealand',
							'South Africa', 'Pakistan'],
			't20': ['Pakistan', 'India', 'Australia',
							'England', 'New Zealand']}

# Convert the dictionary into DataFrame
rankings_pd = pd.DataFrame(rankings)

# Before renaming the columns
print(rankings_pd)
# using rename fuction
rankings_pd.rename(columns = {'test':'TEST','odi':'ODI','t20':'T20'}, inplace = True)
# By assigning list of new column names
rankings_pd.columns = ['TEST', 'ODI', 'T-20']

# using set_axis
rankings_pd.set_axis(['A', 'B', 'C'], axis='columns', inplace=True)

# add prefix and suffix
rankings_pd = rankings_pd.add_prefix('col_')
rankings_pd = rankings_pd.add_suffix('_1')

print(rankings_pd)
