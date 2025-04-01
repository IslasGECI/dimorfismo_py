from dimorfism.adapters import raw_data_adapter


def test_tdp_adapter():
    raw_data_path = "tests/data/tdp_morfometria_albatros.csv"
    obtained = raw_data_adapter(raw_data_path)
    obtained_columns = obtained.columns
    assert "bill_length" in obtained_columns
