import json


def obtained_parameters(fitted_model):
    keys = ["bill_depth", "bill_length", "Tarsus", "head_width", "Intercept"]
    values = [*fitted_model.coef_, *fitted_model.intercept_]
    return {k: v for (k, v) in zip(keys, values)}


def write_json_parameters(parameters_dictionary, parameters_path):
    json_object = json.dumps(parameters_dictionary)
    with open(parameters_path, "w") as outfile:
        outfile.write(json_object)
