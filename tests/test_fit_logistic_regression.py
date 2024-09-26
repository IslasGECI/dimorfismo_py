import numpy
import dimorfism as dt


def test_fit_logistic_regression():
    x = numpy.array(
        [3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]
    ).reshape(-1, 1)
    y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
    logr = dt.logistic_regression()
    logr.fit(x, y)
