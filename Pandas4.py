#Question 1 : 
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee[['salary']].drop_duplicates()
    
    if (N > len(employee)) | (N <= 0) :
        return pd.DataFrame({f'getNthHighestSalary({N})' : [None]})
    employee['rnk'] = employee['salary'].rank(method = 'dense' , ascending = False)
    employee = employee[employee['rnk'] == N]

    return employee[['salary']].rename(columns = {'salary' : f'getNthHighestSalary({N})'})

         
#Question 2 :

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee[['salary']].drop_duplicates()
    if len(employee) < 2 :
        return pd.DataFrame({'SecondHighestSalary' : [None]})
    employee['rnk'] = employee['salary'].rank(method = 'dense' , ascending = False)
    employee = employee[employee['rnk'] == 2]
    return employee[['salary']].rename(columns = {'salary' : 'SecondHighestSalary'})
