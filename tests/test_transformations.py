import pandas as pd
import dummy_transformations as dt


def test_add_offset():
    augend = 1
    addend = 2
    expected = augend + addend
    obtained = dt.add_offset(augend, addend)
    assert expected == obtained


def test_split_data() -> None:
    _ = pd.read_csv("/workdir/tests/data/laysan_albatross_morphometry_guadalupe.csv")
