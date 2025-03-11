from dimorfism.write_parameters import write_model_parameters
import geci_test_tools as gtt


def test_get_model_parameters():
    data_path = "tests/data/laysan_albatross_morphometry_guadalupe.csv"
    parameters_path = "tests/data/model_parameters.json"
    gtt.if_exist_remove(parameters_path)
    write_model_parameters(data_path, parameters_path)
    gtt.assert_exist(parameters_path)
