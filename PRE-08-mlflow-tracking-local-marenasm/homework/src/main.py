## Librerias de mlflow
import os
import uuid
import warnings

import mlflow

warnings.filterwarnings("ignore")

from homework.src._internals.calculate_metrics import calculate_metrics
from homework.src._internals.parse_argument import parse_argument
from homework.src._internals.prepare_data import prepare_data
from homework.src._internals.print_metrics import print_metrics
from homework.src._internals.save_model_if_better import save_model_if_better
from homework.src._internals.select_model import select_model

# import mlflow.sklearn


FILE_PATH = "data/winequality-red.csv"
TEST_SIZE = 0.25
RANDOM_STATE = 123456


def main():

    args = parse_argument()
    model = select_model(args)

    x_train, x_test, y_train, y_test = prepare_data(
        file_path=FILE_PATH,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
    )

    ##
    ## Establece un directorio de usuario para hacer el tracking
    ## de los modelos llamado my_runs. Puede ser un disco de red
    ## o un bucket de S3, por ejemplo.
    ##
    working_directory = os.path.abspath(os.getcwd())
    mlflow_runs_path = os.path.join(working_directory, "my_mlruns")
    if not os.path.exists(mlflow_runs_path):
        os.makedirs(mlflow_runs_path)
    mlflow.set_tracking_uri(mlflow_runs_path)

    ## Autotracking para sklearn
    mlflow.sklearn.autolog(
        log_input_examples=False,
        log_model_signatures=True,
        log_models=True,
        disable=False,
        exclusive=True,
        disable_for_unsupported_versions=False,
        silent=False,
        max_tuning_runs=10,
        log_post_training_metrics=True,
        serialization_format="cloudpickle",
        registered_model_name=None,
    )

    ## Se inicia un experimento en MLflow
    mlflow.set_experiment("wine_quality_experiment")
    run_name = f"{args.model}_{uuid.uuid4().hex[:8]}"
    with mlflow.start_run(run_name=run_name):

        run = mlflow.active_run()
        print()
        print("Active run_id: {}".format(run.info.run_id))

        mlflow.log_param("file_path", FILE_PATH)
        mlflow.log_param("test_size", TEST_SIZE)
        mlflow.log_param("random_state", RANDOM_STATE)
        # mlflow.log_param("model_type", args.model)

        # ## Log de los parametros especificos de cada tipo de modelo
        # if args.model == "elasticnet":
        #     mlflow.log_param("alpha", args.alpha)
        #     mlflow.log_param("l1_ratio", args.l1_ratio)
        # elif args.model == "knn":
        #     mlflow.log_param("n_neighbors", args.n_neighbors)

        model.fit(x_train, y_train)

        mse, mae, r2 = calculate_metrics(model, x_train, y_train)
        print_metrics("Training metrics", mse, mae, r2)

        ## Log de las metricas de entrenamiento
        mlflow.log_metric("train_mse", mse)
        mlflow.log_metric("train_mae", mae)
        mlflow.log_metric("train_r2", r2)

        mse, mae, r2 = calculate_metrics(model, x_test, y_test)
        print_metrics("Testing metrics", mse, mae, r2)

        ## Log de las metricas de test
        mlflow.log_metric("test_mse", mse)
        mlflow.log_metric("test_mae", mae)
        mlflow.log_metric("test_r2", r2)

        ## Ya no se requiere
        # save_model_if_better(model, x_test, y_test)


if __name__ == "__main__":
    main()
