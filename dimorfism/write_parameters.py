def obtained_parameters(fitted_model):
    keys = ["bill_depth", "bill_length", "Tarsus", "head_width", "Intercept"]
    values = [*fitted_model.coef_, *fitted_model.intercept_]
    return {k: v for (k, v) in zip(keys, values)}
