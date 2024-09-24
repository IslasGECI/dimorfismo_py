import pandas as pd


def split_data(df: pd.DataFrame) -> dict:
    splitted_data = {"to_test": df[:3]}

    return splitted_data
