import pandas as pd
from sklearn.model_selection import train_test_split


def split_data(df: pd.DataFrame) -> dict:
    target = df["sexo"]
    data_train, data_test, target_train, target_test = train_test_split(
        df, target, random_state=7, train_size=0.8
    )
    not_wanted_colnames: list = ["id_nido", "id_darvic", "subcolonia", "temporada", "notas"]
    not_wanted_colnames_tests: list = [
        "id_nido",
        "id_darvic",
        "subcolonia",
        "temporada",
        "notas",
        "sexo",
    ]
    splitted_data = {
        "to_fit": data_train.drop(columns=not_wanted_colnames),
        "to_test": data_test.drop(columns=not_wanted_colnames_tests),
        "to_test_y": pd.DataFrame(target_test),
    }

    return splitted_data


def extract_sample_to_fit(df):
    return df.sample(frac=0.8, random_state=7)


def obtained_to_test_data(df: pd.DataFrame) -> pd.DataFrame:

    to_test = df.drop(extract_sample_to_fit(df).index)

    not_wanted_colnames: list = ["id_nido", "id_darvic", "subcolonia", "temporada", "notas", "sexo"]

    return to_test.drop(columns=not_wanted_colnames)


def obtained_to_test_data_y(df: pd.DataFrame) -> pd.DataFrame:

    to_test = df.drop(extract_sample_to_fit(df).index)

    return to_test[["sexo"]]
