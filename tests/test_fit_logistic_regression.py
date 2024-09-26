import numpy
import pytest
import dimorfism as dt


def test_logistic_regression():
    x = numpy.array(
        [3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]
    ).reshape(-1, 1)
    y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
    logr = dt.logistic_regression()
    logr.fit(x, y)
    expected = [0]
    obtained = logr.predict(numpy.array([3.46]).reshape(-1, 1))
    assert expected == obtained, "First example of w3school"
    log_odds = logr.coef_
    expected_odd = numpy.array([[4.035]])
    obtained_odd = numpy.exp(log_odds)
    assert expected_odd == pytest.approx(obtained_odd, 0.1), "Second example of w3school"
