import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    column_name = f'getNthHighestSalary({N})'
    unique_salaries = employee['salary'].drop_duplicates()
    sorted_salaries = unique_salaries.sort_values(ascending=False)
    if len(sorted_salaries)<N:
        return  pd.DataFrame({column_name: [None]})

    nth_highest = sorted_salaries.iloc[N - 1]

    return pd.DataFrame({column_name: [nth_highest]})