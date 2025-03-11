from dimorfism.cli import write_model_parameters, app

import geci_test_tools as gtt
from typer.testing import CliRunner


def test_get_model_parameters():
    data_path = "tests/data/laysan_albatross_morphometry_guadalupe.csv"
    parameters_path = "tests/data/model_parameters.json"
    gtt.if_exist_remove(parameters_path)
    write_model_parameters(data_path, parameters_path)
    gtt.assert_exist(parameters_path)


runner = CliRunner()


def tests_write_model_parameters():
    result = runner.invoke(app, ["write-model-parameters", "--help"])
    assert result.exit_code == 0
    assert "--data-path" in result.stdout
    assert "Input morphometry data path" in result.stdout


def test_version():
    result = runner.invoke(
        app,
        ["version"],
    )
    expected_version = "0.0.1"
    assert expected_version in result.stdout
