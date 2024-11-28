import dimorfism as dt


coeficients = [1.26, 3.45, 4.25, 7.81]


def test_obtained_parameters():
    fitted_model = Mock_fitted_model()
    obtained = dt.obtained_parameters(fitted_model)
    isinstance(obtained, dict)
    assert list(obtained.keys()) == [
        "bill_depth",
        "bill_length",
        "Tarsus",
        "head_width",
        "Intercept",
    ]

    assert list(obtained.values()) == coeficients


class Mock_fitted_model:
    def __init__(self):
        self.intercept_ = [-12.466]
        self.coef_ = coeficients
