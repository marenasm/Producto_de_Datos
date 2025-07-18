import mlflow
import pandas as pd
from sklearn.model_selection import train_test_split


def predict():

    file_path = "data/winequality-red.csv"
    df = pd.read_csv(file_path)
    y = df["quality"]
    x = df.drop(columns=["quality"])

    model_name = "my-regression-model"
    model_version = 1

    model = mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{model_version}")

    return model.predict(x[0:10])


print(predict())
