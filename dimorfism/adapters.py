import pandas as pd


def adapter_morphometry(data_path):
    wanted_colnames: list = [
        "bill_depth",
        "bill_length",
        "head_width",
        "Tarsus",
    ]
    complete_dataframe = pd.read_csv(data_path)
    complete_dataframe = xxraw_data_adapter(complete_dataframe)
    return complete_dataframe[wanted_colnames + ["sexo"]]


def raw_data_adapter(raw_data_path):
    data = pd.read_csv(raw_data_path)
    return xxraw_data_adapter(data)


def xxraw_data_adapter(raw_data):
    data = raw_data
    name_equivalents = {
        "longitudPico": "bill_length",
        "altoPico": "bill_depth",
        "anchoCraneo": "head_width",
        "tarso": "Tarsus",
    }
    return data.rename(columns=name_equivalents)
