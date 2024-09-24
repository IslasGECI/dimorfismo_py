import pandas as pd
import pytest
import dimorfism as dt


def test_split_data() -> None:
    full_data: pd.DataFrame = pd.read_csv(
        "/workdir/tests/data/laysan_albatross_morphometry_guadalupe.csv"
    )
    splited_data: dict = dt.split_data(full_data)
    test_data: pd.DataFrame = splited_data["to_test"]
    expected_n_row: int = 3
    assert len(test_data) == expected_n_row, "The number of row is right"
    fit_data: pd.DataFrame = splited_data["to_fit"]
    _check_number_of_row_is_right(fit_data, 12)


@pytest.mark.xfail(strict=True)
def test_split_data_are_differents() -> None:
    full_data: pd.DataFrame = pd.read_csv(
        "/workdir/tests/data/laysan_albatross_morphometry_guadalupe.csv"
    )
    splited_data: dict = dt.split_data(full_data)
    fit_data: pd.DataFrame = splited_data["to_fit"]
    pd.testing.assert_frame_equal(full_data[:12], fit_data)


@pytest.mark.xfail(strict=True)
def test_split_data_are_differents_to_Test() -> None:
    full_data: pd.DataFrame = pd.read_csv(
        "/workdir/tests/data/laysan_albatross_morphometry_guadalupe.csv"
    )
    splited_data: dict = dt.split_data(full_data)
    test_data: pd.DataFrame = splited_data["to_test"]
    pd.testing.assert_frame_equal(full_data[12:], test_data)


def test_split_data_are_differents_rows() -> None:
    full_data: pd.DataFrame = pd.read_csv(
        "/workdir/tests/data/laysan_albatross_morphometry_guadalupe.csv"
    )
    splited_data: dict = dt.split_data(full_data)
    test_data: pd.DataFrame = splited_data["to_test"]
    fit_data: pd.DataFrame = splited_data["to_fit"]
    index_to_fit = set(fit_data.index)
    index_to_test = set(test_data.index)
    obtained_commun = len(index_to_fit and index_to_test)
    expected_commun = 0
    assert obtained_commun == expected_commun


def _check_number_of_row_is_right(data: pd.DataFrame, expected_n_row: int) -> None:
    obtained_n_row: int = len(data)
    assert obtained_n_row == expected_n_row, "The number of row is right"
