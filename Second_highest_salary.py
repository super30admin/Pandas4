import pandas as pd
import numpy as np

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.drop_duplicates(['salary'],inplace=True)
    employee['rank'] = employee['salary'].rank(method = 'dense', ascending = False)
    if max(employee['rank']) < 2:
        return pd.DataFrame([np.NaN],columns = ['SecondHighestSalary'])
    return employee[employee['rank'] == 2][['salary']].rename(columns = {'salary':'SecondHighestSalary'})
