from sklearn import linear_model
import pandas as pd


def predicted_sex(splited_data: pd.DataFrame):
    model = logistic_regression()
    x = splited_data["to_fit"].drop(columns="sexo")
    y = splited_data["to_fit"]["sexo"]
    return model.fit(x, y)


def logistic_regression():
    return linear_model.LogisticRegression()
