import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # Use a regex that specifically looks for:
    # ^DIAB1 -> Starts with DIAB1 at the beginning of the column
    # |      -> OR
    # \sDIAB1 -> A space followed by DIAB1
    pattern = r'^DIAB1|\sDIAB1'
    
    # Filter the dataframe
    result = patients[patients['conditions'].str.contains(pattern, regex=True)]
    
    return result[['patient_id', 'patient_name', 'conditions']]