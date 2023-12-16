import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # retrieve all unique values, sort them desc and pick N-1 th Value from the list
    df = employee.drop_duplicates(['salary'])

    ######### Scenario 2 Null Check ############
    if ((len(df) < N) | (N <= 0)):
        return pd.DataFrame({f'getNthHighestSalary({N})' : [None] })
    
    # Scenarios 1 sort Values
    df = df.sort_values(by = ['salary'], ascending = False)
    
        # df['rnk'] = df['salary'].rank(method = 'dense', ascending = False)
        # df  = df[df ['rnk'] == N]

    return df[['salary']].head(N).tail(1).rename(columns = {'salary': f'getNthHighestSalary({N})'})