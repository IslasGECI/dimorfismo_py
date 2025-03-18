from dimorfism.write_parameters import xxget_model_parameters, write_json_parameters
import pandas as pd

import typer

app = typer.Typer()


@app.command()
def write_model_parameters(
    data_path: str = typer.Option("Input morphometry data path"),
    parameters_path: str = typer.Option("Output parameters path"),
):
    wanted_colnames: list = [
        "bill_depth",
        "bill_length",
        "head_width",
        "Tarsus",
    ]
    complete_dataframe = pd.read_csv(data_path)
    parameters_dictionary = xxget_model_parameters(complete_dataframe, wanted_colnames)
    write_json_parameters(parameters_dictionary, parameters_path)


@app.command()
def version():
    print("0.0.1")
