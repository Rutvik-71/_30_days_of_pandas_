import pandas as pd

def delete_duplicate_emails(Person: pd.DataFrame) -> None:
    Person.sort_values(by="id", inplace=True)
    Person.drop_duplicates(subset="email", keep="first", inplace=True)
