#Problem 1 : Get all rows in a Pandas DataFrame containing given substring
import pandas as pd
df = pd.DataFrame({'Name':['Taylor','Selena','Haylay'],'Lyrics':['All this people','people can go','Without me']})
df1 = df[df['Lyrics'].str.contains("people")]
print(df1)
#Problem 2 : Create a pandas column using for loop
import pandas as pd

df = pd.DataFrame({'Name':['Taylor','Selena','Haylay'],'Lyrics':['All this people','people can go','Without me'],'Ratings':[4.5,4,3]})
ratings = []
  
for rating in df['Ratings']:       
    if rating >= 3.5:
        ratings.append('Good')
    elif rating < 3.5:
        ratings.append("Bad")
    else:
        ratings.append("Not Sure")

df['Ratings'] = ratings  
            
print(df)
#Problem 3 : How to get column names in Pandas dataframe
import pandas as pd

df = pd.DataFrame({'Name':['Taylor','Selena','Haylay'],'Lyrics':['All this people','people can go','Without me'],'Ratings':[4.5,4,3]})
print(list(df.columns))
#Problem 4 : How to rename columns in Pandas DataFrame
import pandas as pd

df = pd.DataFrame({'Name':['Taylor','Selena','Haylay'],'Lyrics':['All this people','people can go','Without me'],'Ratings':[4.5,4,3]})
df.rename(columns = {'Ratings':'Spotify_ranks'}, inplace = True)
print(df)
#Problem 5 : Get unique values from a column in Pandas DataFrame 
import pandas as pd

df = pd.DataFrame({'Name':['Taylor','Selena','Haylay'],'Lyrics':['All this people','people can go','Without me'],'Ratings':[4.5,4.5,3.0]})
print(df.Ratings.unique())
