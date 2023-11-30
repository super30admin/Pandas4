import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee.drop_duplicates(['salary'])
    if len(df)< N:
        return pd.DataFrame({f'getNthHighestSalary({N})':[None]})
    df.sort_values(by = ['salary'], ascending = False, inplace = True)
    return df[['salary']].head(N).tail(1).rename(columns = {'salary':f'getNthHighestSalary({N})'})