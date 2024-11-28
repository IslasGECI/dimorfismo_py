import dimorfism as dt


def test_obtained_parameters():
    fitted_model = Mock_fitted_model()
    obtained = dt.obtained_parameters(fitted_model)
    isinstance(obtained, dict)
    assert list(obtained.keys()) == ["bill_depth", "bill_length", "Tarsus", "head_width"]


class Mock_fitted_model:
    def __init__(self):
        self.intercept_ = [1.26]
        self.coef_ = [1.26, 3.45]
