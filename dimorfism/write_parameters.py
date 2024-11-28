def obtained_parameters(fitted_model):
    keys = ["bill_depth", "bill_length", "Tarsus", "head_width"]
    values = fitted_model.coef_
    myDict = {k: v for (k, v) in zip(keys, values)}
    myDict["Intercept"] = fitted_model.intercept_[0]
    return myDict
