import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result = customers[~customers['id'].isin(orders['customerId'])]
    return result[['name']].rename(columns={'name': 'Customers'})
