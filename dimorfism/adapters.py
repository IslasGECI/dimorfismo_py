import pandas as pd


def adapter_morphometry(data_path):
    wanted_colnames: list = [
        "bill_depth",
        "bill_length",
        "head_width",
        "Tarsus",
    ]
    complete_dataframe = pd.read_csv(data_path)
    complete_dataframe = translate_columns(complete_dataframe)
    return complete_dataframe[wanted_colnames + ["sexo"]]


def translate_columns(raw_data):
    data = raw_data
    name_equivalents = {
        "longitudPico": "bill_length",
        "altoPico": "bill_depth",
        "anchoCraneo": "head_width",
        "tarso": "Tarsus",
    }
    return data.rename(columns=name_equivalents)
