import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = pd.DataFrame(employee['salary'].unique(),columns=['salary']) 
    #employee.drop_duplicates(['salary'])
    if len(df) <  N:
        return pd.DataFrame({f'getNthHighestSalary({N})' : [None]})
    df = df.sort_values(by = ['salary'],ascending = False)
    return df[['salary']].head(N).tail(1).rename(columns = {'salary':f'getNthHighestSalary({N})'})