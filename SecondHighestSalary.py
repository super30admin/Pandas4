import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.drop_duplicates(['salary']).sort_values(by='salary', ascending=False)
    if len(df) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})

    second_highest_salary = df.iloc[1]['salary']
    return pd.DataFrame({'SecondHighestSalary': [second_highest_salary]})

