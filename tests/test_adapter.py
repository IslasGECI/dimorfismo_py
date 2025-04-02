from dimorfism.adapters import xxraw_data_adapter
import pandas as pd


def test_tdp_adapter():
    raw_data_path = "tests/data/tdp_morfometria_albatros.csv"
    raw_data = pd.read_csv(raw_data_path)
    obtained = xxraw_data_adapter(raw_data)
    obtained_columns = set(obtained.columns)
    expected_columns = set(["bill_length", "bill_depth", "head_width", "Tarsus"])
    assert expected_columns.issubset(obtained_columns)
