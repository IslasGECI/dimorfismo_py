import numpy as np
import dimorfism as dt


coeficients = [1.26, 3.45, 4.25, 7.81]
intercept = [-12.466]


def test_obtained_parameters():
    fitted_model = Mock_fitted_model()
    obtained = dt.obtained_parameters(fitted_model)
    isinstance(obtained, dict)
    assert list(obtained.keys()) == [
        "bill_depth",
        "bill_length",
        "head_width",
        "Tarsus",
        "Intercept",
    ]

    assert list(obtained.values()) == [*coeficients, *intercept]


class Mock_fitted_model:
    def __init__(self):
        self.feature_names_in_ = np.array(["bill_depth", "bill_length", "head_width", "Tarsus"])
        self.intercept_ = np.array([intercept])
        self.coef_ = np.array([coeficients])
