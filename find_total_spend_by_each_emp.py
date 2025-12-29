import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees["total_time"] = employees["out_time"] - employees["in_time"]
    
    return (
        employees
        .groupby(["event_day", "emp_id"], as_index=False)
        .agg(total_time=("total_time", "sum"))
        .rename(columns={"event_day": "day"})
    )