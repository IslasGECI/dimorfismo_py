import pandas as pd
import dimorfism as dt


def test_split_data() -> None:
    full_data: pd.DataFrame = pd.read_csv(
        "/workdir/tests/data/laysan_albatross_morphometry_guadalupe.csv"
    )
    splited_data: dict = dt.split_data(full_data)
    test_data: pd.DataFrame = splited_data["to_test"]
    expected_n_row = 3
    assert len(test_data) == expected_n_row, "The number of row is right"
    fit_data: pd.DataFrame = splited_data["to_fit"]
    expected_n_row_to_fit = 12
    assert len(fit_data) == expected_n_row_to_fit, "The number of row to fit is right"
