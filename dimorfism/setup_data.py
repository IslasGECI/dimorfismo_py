import pandas as pd
from sklearn.model_selection import train_test_split


def split_data(df: pd.DataFrame) -> dict:
    target_name = "sexo"
    target = df[target_name]
    data_train, data_test, target_train, target_test = train_test_split(
        df, target, random_state=7, train_size=0.8
    )
    print(data_train)
    not_wanted_colnames: list = ["id_nido", "id_darvic", "subcolonia", "temporada", "notas"]
    not_wanted_colnames_tests = not_wanted_colnames + [target_name]
    splitted_data = {
        "to_fit": data_train.drop(columns=not_wanted_colnames),
        "to_fit_target": target_train,
        "to_test": data_test.drop(columns=not_wanted_colnames_tests),
        "to_test_y": pd.DataFrame(target_test),
    }

    return splitted_data
