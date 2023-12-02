import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee["rnk"] = employee["salary"].rank(method='dense', ascending=False)
    df = employee.sort_values(by="rnk", ascending=False)
    df = df[df["rnk"] == N]
    df = df.head(1)
    df = df.rename(columns={"salary":"getNthHighestSalary"})
    res = df[["getNthHighestSalary"]]
    if res.shape[0] == 0:
        data = {'getNthHighestSalary': [None]}
        return pd.DataFrame(data)
    else:
        return res