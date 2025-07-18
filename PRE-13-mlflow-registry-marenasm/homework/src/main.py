## Se importa MLflow
import mlflow

from ._internals.calculate_metrics import calculate_metrics
from ._internals.parse_argument import parse_argument
from ._internals.prepare_data import prepare_data
from ._internals.print_metrics import print_metrics
from ._internals.save_model_if_better import save_model_if_better
from ._internals.select_model import select_model

FILE_PATH = "data/winequality-red.csv"
TEST_SIZE = 0.25
RANDOM_STATE = 123456


def main():

    args = parse_argument()
    model = select_model(args)

    x_train, x_test, y_train, y_test = prepare_data(
        FILE_PATH,
        TEST_SIZE,
        RANDOM_STATE,
    )

    print("Tracking directory:", mlflow.get_tracking_uri())
    with mlflow.start_run():

        mlflow.log_param("file_path", FILE_PATH)
        mlflow.log_param("test_size", TEST_SIZE)
        mlflow.log_param("random_state", RANDOM_STATE)
        mlflow.log_param("model_type", args.model)

        if args.model == "elasticnet":
            mlflow.log_param("alpha", args.alpha)
            mlflow.log_param("l1_ratio", args.l1_ratio)
        elif args.model == "knn":
            mlflow.log_param("n_neighbors", args.n_neighbors)

        model.fit(x_train, y_train)

        mse, mae, r2 = calculate_metrics(model, x_train, y_train)
        print_metrics("Training metrics", mse, mae, r2)

        mlflow.log_metric("train_mse", mse)
        mlflow.log_metric("train_mae", mae)
        mlflow.log_metric("train_r2", r2)

        mse, mae, r2 = calculate_metrics(model, x_test, y_test)
        print_metrics("Testing metrics", mse, mae, r2)

        mlflow.log_metric("test_mse", mse)
        mlflow.log_metric("test_mae", mae)
        mlflow.log_metric("test_r2", r2)

        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="model",
            input_example=x_train[:1],
        )


if __name__ == "__main__":
    main()
