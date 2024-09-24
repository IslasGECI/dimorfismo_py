import pandas as pd
import dummy_transformations as dt


def test_add_offset():
    augend = 1
    addend = 2
    expected = augend + addend
    obtained = dt.add_offset(augend, addend)
    assert expected == obtained


def test_split_data() -> None:
    full_data = pd.read_csv("/workdir/tests/data/laysan_albatross_morphometry_guadalupe.csv")
    _ = dt.split_data()
