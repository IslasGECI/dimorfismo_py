from sklearn import linear_model
import pandas as pd


def predicted_sex(splited_data: pd.DataFrame):
    model = logistic_regression()
    x = splited_data["to_fit"].drop(columns="sexo")
    y = splited_data["to_fit"]["sexo"]
    fitted_model = model.fit(x, y)

    to_predict = splited_data["to_test"]
    return fitted_model.predict(to_predict)


def logistic_regression():
    return linear_model.LogisticRegression()
