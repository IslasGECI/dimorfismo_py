from sklearn import linear_model
import pandas as pd


def predicted_sex(splited_data: pd.DataFrame):
    fitted_model = get_fitted_model(splited_data)

    to_predict = splited_data["to_test"]
    return fitted_model.predict(to_predict)


def get_fitted_model(splited_data):
    model = logistic_regression()
    x = splited_data["to_fit"]
    y = splited_data["to_fit_target"]
    fitted_model = model.fit(x, y)
    return fitted_model


def logistic_regression():
    return linear_model.LogisticRegression()
