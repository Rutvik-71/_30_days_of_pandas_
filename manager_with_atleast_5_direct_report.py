def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
   
    counts = employee['managerId'].value_counts()
    valid_managers = counts[counts >= 5].index

    return employee[employee['id'].isin(valid_managers)][['name']]