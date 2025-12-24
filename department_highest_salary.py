import pandas as pd

def department_highest_salary(employee: pd.DataFrame,
                              department: pd.DataFrame) -> pd.DataFrame:
    

    max_salary = employee.groupby("departmentId", as_index=False)["salary"].max()
    
   
    merged = employee.merge(
        max_salary,
        on=["departmentId", "salary"],
        how="inner"
    )
    
    result = merged.merge(
        department,
        left_on="departmentId",
        right_on="id",
        how="inner"
    )
    
    return result[["name_x", "salary", "name_y"]].rename(
        columns={
            "name_x": "Employee",
            "salary": "Salary",
            "name_y": "Department"
        }
    )
