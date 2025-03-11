import numpy as np
import dimorfism as dt
import geci_test_tools as gtt


def test_get_model_parameters():
    data_path = "tests/data/laysan_albatross_morphometry_guadalupe.csv"
    parameters_path = "tests/data/model_parameters.json"
    gtt.if_exist_remove(parameters_path)
    dt.get_model_parameters(data_path, parameters_path)
    gtt.assert_exist(parameters_path)


def test_write_json_parameters():
    parameters_dictionary = {"Intercept": 1, "parameter_1": 8.4}
    parameters_path = "tests/data/model_parameters.json"
    gtt.if_exist_remove(parameters_path)
    dt.write_json_parameters(parameters_dictionary, parameters_path)
    gtt.assert_exist(parameters_path)


coeficients = [1.26, 3.45, 4.25, 7.81]
intercept = [-12.466]


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

    assert list(obtained.values()) == [*coeficients, *intercept]


class Mock_fitted_model:
    def __init__(self):
        self.intercept_ = np.array([intercept])
        self.coef_ = np.array([coeficients])
