'''
1. We create a column in df by first creating a list with a filtering condition on a column age.
2. Then we add the list as a column Voter in the dataframe
'''
import pandas as pd
import numpy as np

raw_Data = {'Voter_name': ['Geek1', 'Geek2', 'Geek3', 'Geek4',
						'Geek5', 'Geek6', 'Geek7', 'Geek8'],
			'Voter_age': [15, 23, 25, 9, 67, 54, 42, np.NaN]}

# Creating a df using constructor
df = pd.DataFrame(raw_Data, columns = ['Voter_name', 'Voter_age'])

# Empty list for storing the eligibility to vote
eligible = []

for age in df['Voter_age']:	
	if age >= 18:				
		eligible.append('Yes')
	elif age < 18:				 
		eligible.append("No")
	else:
		eligible.append("Not Sure")

# Create a column from the list
df['Voter'] = eligible
			
print(df)
