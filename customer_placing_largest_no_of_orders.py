import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return (
        orders
        .groupby("customer_number", as_index=False)
        .size()
        .sort_values("size", ascending=False)
        .head(1)[["customer_number"]]
    )

