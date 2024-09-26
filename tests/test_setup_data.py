import pandas as pd
import pytest
import dimorfism as dt

full_data: pd.DataFrame = pd.read_csv(
    "/workdir/tests/data/laysan_albatross_morphometry_guadalupe.csv"
)
splited_data: dict = dt.split_data(full_data)


def test_split_data() -> None:
    test_data: pd.DataFrame = splited_data["to_test"]
    _check_number_of_row_is_right(test_data, 3)

    test_data_y: pd.DataFrame = splited_data["to_test_y"]
    _check_number_of_row_is_right(test_data_y, 3)

    test_data: pd.DataFrame = splited_data["to_test"]
    fit_data: pd.DataFrame = splited_data["to_fit"]
    _check_number_of_row_is_right(fit_data, 12)


def test_test_data_sexo():
    test_data_y: pd.DataFrame = splited_data["to_test_y"]
    expected = "sexo"
    obatined = test_data_y.columns
    assert obatined == expected


@pytest.mark.xfail(strict=True)
def test_split_data_are_differents() -> None:
    fit_data: pd.DataFrame = splited_data["to_fit"]
    pd.testing.assert_frame_equal(full_data[:12], fit_data)


def test_split_data_with_right_columns() -> None:
    fit_data: pd.DataFrame = splited_data["to_fit"]
    obtained_colname = fit_data.columns
    not_expexted_colname = {"id_nido", "id_darvic", "subcolonia", "temporada", "notas"}
    obtained_commun = len(not_expexted_colname & set(obtained_colname))
    expected_commun = 0
    assert obtained_commun == expected_commun


@pytest.mark.xfail(strict=True)
def test_split_data_are_differents_to_Test() -> None:
    test_data: pd.DataFrame = splited_data["to_test"]
    pd.testing.assert_frame_equal(full_data[12:], test_data)


def test_split_test_data_with_right_columns() -> None:
    test_data: pd.DataFrame = splited_data["to_test"]
    obtained_colname = test_data.columns
    not_expexted_colname = {"id_nido", "id_darvic", "subcolonia", "temporada", "notas", "sexo"}
    obtained_commun = len(not_expexted_colname & set(obtained_colname))
    expected_commun = 0
    assert obtained_commun == expected_commun


def test_split_data_are_differents_rows() -> None:
    test_data: pd.DataFrame = splited_data["to_test"]
    fit_data: pd.DataFrame = splited_data["to_fit"]
    index_to_fit = set(fit_data.index)
    index_to_test = set(test_data.index)
    obtained_commun = len(index_to_fit & index_to_test)
    expected_commun = 0
    assert obtained_commun == expected_commun


def _check_number_of_row_is_right(data: pd.DataFrame, expected_n_row: int) -> None:
    obtained_n_row: int = len(data)
    assert obtained_n_row == expected_n_row, "The number of row is right"
