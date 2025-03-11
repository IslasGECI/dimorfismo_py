import json
from dimorfism.setup_data import split_data
from dimorfism.fit_logistic_regression import get_fitted_model
import pandas as pd


def obtained_parameters(fitted_model):
    keys = ["bill_depth", "bill_length", "Tarsus", "head_width", "Intercept"]
    values = [*fitted_model.coef_[0], *fitted_model.intercept_]
    return {k: float(v) for (k, v) in zip(keys, values)}


def write_json_parameters(parameters_dictionary, parameters_path):
    with open(parameters_path, "w") as outfile:
        json.dump(parameters_dictionary, outfile)


def write_model_parameters(data_path, parameters_path):
    complete_dataframe = pd.read_csv(data_path)
    parameters_dictionary = calculate_model_parameters(complete_dataframe)
    write_json_parameters(parameters_dictionary, parameters_path)


def calculate_model_parameters(complete_dataframe):
    splited_data = split_data(complete_dataframe)
    fitted_model = get_fitted_model(splited_data)
    parameters_dictionary = obtained_parameters(fitted_model)
    return parameters_dictionary
