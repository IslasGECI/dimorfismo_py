from dimorfism.write_parameters import get_model_parameters, write_json_parameters
import pandas as pd

import typer

app = typer.Typer()


@app.command()
def write_model_parameters(data_path, parameters_path):
    complete_dataframe = pd.read_csv(data_path)
    parameters_dictionary = get_model_parameters(complete_dataframe)
    write_json_parameters(parameters_dictionary, parameters_path)
