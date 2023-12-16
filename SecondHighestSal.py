import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame: 
    # retrieve all unique values, sort them desc and pick N-1 th Value from the list
    df = employee.drop_duplicates(['salary'])

    ######### Scenario 2 Null Check ############
    if ((len(df) < 2)):
        return pd.DataFrame('SecondHighestSalary' : [None] )
    
    # Scenarios 1 sort Values
    df = df.sort_values(by = ['salary'], ascending = False)
    
    return df[['salary']].head(2).tail(1).rename(columns = {'salary': 'SecondHighestSalary'})