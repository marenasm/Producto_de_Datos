"""Grading"""

import os
import subprocess
import warnings

warnings.filterwarnings("ignore")


def test_01():

    # Test if the homework script runs without errors
    try:
        for entry_point in ["elasticnet", "knn"]:
            subprocess.run(
                [
                    "mlflow",
                    "run",
                    "--env-manager=local",
                    "-e",
                    entry_point,
                    ".",
                ],
                check=True,
            )
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error running the homework script: {e}")

    # Ensure the mlruns directory exists
    assert os.path.exists("mlruns"), "mlruns directory does not exist."

    # Check if there are any experiments saved in mlruns/
    experiments = [
        d for d in os.listdir("mlruns") if os.path.isdir(os.path.join("mlruns", d))
    ]
    assert len(experiments) > 0, "No experiments found in mlruns directory."
