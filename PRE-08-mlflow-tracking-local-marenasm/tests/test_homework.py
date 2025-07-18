"""Grading"""

import os
import subprocess
import warnings

warnings.filterwarnings("ignore")


def test_01():

    # Test if the homework script runs without errors
    try:
        for model in ["elasticnet", "knn"]:
            subprocess.run(
                ["python3", "-m", "homework", "--model", model],
                check=True,
            )
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error running the homework script: {e}")

    # Ensure the mlruns directory exists
    assert os.path.exists("my_mlruns"), "mlruns directory does not exist."

    # Check if there are any experiments saved in mlruns/
    experiments = [
        d
        for d in os.listdir("my_mlruns")
        if os.path.isdir(os.path.join("my_mlruns", d))
    ]
    assert len(experiments) > 0, "No experiments found in my_mlruns directory."
