import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee['rnk'] = employee['salary'].rank(method='dense', ascending=False)
    df = employee[employee['rnk'] == 2]
    result_df = pd.DataFrame(df['salary'], columns=['salary'])
    result_df = result_df.rename(columns={'salary': 'SecondHighestSalary'})
    if result_df.empty:
        return pd.DataFrame([np.nan], columns=['SecondHighestSalary'])
    else:
        return pd.DataFrame(result_df['SecondHighestSalary'].unique(), columns=['SecondHighestSalary'])
