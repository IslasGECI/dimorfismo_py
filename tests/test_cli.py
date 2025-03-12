from dimorfism.cli import write_model_parameters, app
import json

import geci_test_tools as gtt
from typer.testing import CliRunner


runner = CliRunner()


def tests_write_model_parameters():
    result = runner.invoke(app, ["write-model-parameters", "--help"])
    assert result.exit_code == 0
    assert "--data-path" in result.stdout
    assert " Input morphometry data path]" in result.stdout
    assert "--parameters-path" in result.stdout
    assert " Output parameters path]" in result.stdout

    data_path = "tests/data/laysan_albatross_morphometry_guadalupe.csv"
    parameters_path = "tests/data/cli_model_parameters.json"

    gtt.if_exist_remove(parameters_path)
    result = runner.invoke(
        app,
        ["write-model-parameters", "--data-path", data_path, "--parameters-path", parameters_path],
    )
    assert result.exit_code == 0
    gtt.assert_exist(parameters_path)

    parameters = read_json(parameters_path)

    assert set(parameters.keys()) == set(
        ["bill_depth", "bill_length", "Tarsus", "head_width", "Intercept"]
    )

    gtt.if_exist_remove(parameters_path)


def test_version():
    result = runner.invoke(
        app,
        ["version"],
    )
    expected_version = "0.0.1"
    assert expected_version in result.stdout


def read_json(json_path):
    with open(json_path, "r") as file:
        data = json.load(file)
    return data
