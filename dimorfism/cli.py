from dimorfism.write_parameters import get_model_parameters, write_json_parameters
from dimorfism.adapters import adapter_morphometry, translate_columns

import typer

app = typer.Typer()


@app.command()
def write_model_parameters(
    data_path: str = typer.Option("Input morphometry data path"),
    parameters_path: str = typer.Option("Output parameters path"),
):
    selected_dataframe = adapter_morphometry(data_path)
    selected_dataframe = translate_columns(selected_dataframe)
    parameters_dictionary = get_model_parameters(selected_dataframe)
    write_json_parameters(parameters_dictionary, parameters_path)


@app.command()
def version():
    print("0.1.0")
