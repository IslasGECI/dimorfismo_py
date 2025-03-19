import pandas as pd
import numpy
import pytest
from dimorfism.fit_logistic_regression import get_fitted_model, logistic_regression
from dimorfism.setup_data import split_data


def test_logistic_regression():
    x = numpy.array(
        [3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]
    ).reshape(-1, 1)
    y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
    logr = logistic_regression()
    logr.fit(x, y)
    expected = [0]
    obtained = logr.predict(numpy.array([3.46]).reshape(-1, 1))
    assert expected == obtained, "First example of w3school"
    log_odds = logr.coef_
    expected_odd = numpy.array([[4.035]])
    obtained_odd = numpy.exp(log_odds)
    assert expected_odd == pytest.approx(obtained_odd, 0.1), "Second example of w3school"


full_data: pd.DataFrame = pd.read_csv(
    "/workdir/tests/data/laysan_albatross_morphometry_guadalupe.csv"
)

wanted_colnames: list = [
    "bill_depth",
    "bill_length",
    "head_width",
    "Tarsus",
]

filtered_data = full_data[wanted_colnames + ["sexo"]]
splited_data: dict = split_data(filtered_data)


def test_albatross_example():
    fitted_model = get_fitted_model(splited_data)
    expected_score = 2 / 3
    x_score = splited_data["to_test"]
    y_score = splited_data["to_test_y"]
    obtained_score = fitted_model.score(x_score, y_score)
    assert obtained_score >= expected_score, "score"
