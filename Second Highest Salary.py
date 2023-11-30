df = employee.drop_duplicates(['salary'])
    if len(df)< 2:
        return pd.DataFrame({'SecondHighestSalary':[None]})
    df.sort_values(by = ['salary'], ascending = False, inplace = True)
    return df[['salary']].head(2).tail(1).rename(columns = {'salary':'SecondHighestSalary'})