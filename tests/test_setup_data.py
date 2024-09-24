import pandas as pd
import dimorfism as dt


def test_split_data() -> None:
    full_data: pd.DataFrame = pd.read_csv(
        "/workdir/tests/data/laysan_albatross_morphometry_guadalupe.csv"
    )
    splited_data: dict = dt.split_data(full_data)
    splited_data["to_test"]
