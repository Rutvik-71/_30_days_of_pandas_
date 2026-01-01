import pandas as pd
def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    return (
        courses
        .groupby("class", as_index=False)
        .size()
        .query("size >= 5")
        [["class"]]
    )

   