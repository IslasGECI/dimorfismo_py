import pandas as pd


def split_data(df: pd.DataFrame) -> dict:
    splitted_data = {"to_fit": df[:12], "to_test": df[12:]}

    return splitted_data
