import pandas as pd


def split_data(df: pd.DataFrame) -> dict:
    splitted_data = {
        "to_fit": obtained_to_fit_data(df),
        "to_test": obtained_to_test_data(df),
        "to_test_y": obtained_to_test_data_y(df),
    }

    return splitted_data


def obtained_to_fit_data(df: pd.DataFrame) -> pd.DataFrame:

    to_fit = df.sample(frac=0.8, random_state=7)

    not_wanted_colnames: list = ["id_nido", "id_darvic", "subcolonia", "temporada", "notas"]

    return to_fit.drop(columns=not_wanted_colnames)


def obtained_to_test_data(df: pd.DataFrame) -> pd.DataFrame:

    to_test = df.drop(df.sample(frac=0.8, random_state=7).index)

    not_wanted_colnames: list = ["id_nido", "id_darvic", "subcolonia", "temporada", "notas", "sexo"]

    return to_test.drop(columns=not_wanted_colnames)


def obtained_to_test_data_y(df: pd.DataFrame) -> pd.DataFrame:

    to_test = df.drop(df.sample(frac=0.8, random_state=7).index)

    return to_test[["sexo"]]
