import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    red_id = company[company['name'] == 'RED']['com_id']
    
    invalid_sales_ids = orders[orders['com_id'].isin(red_id)]['sales_id'].unique()
    
  
    result = sales_person[~sales_person['sales_id'].isin(invalid_sales_ids)]
    
    return result[['name']]