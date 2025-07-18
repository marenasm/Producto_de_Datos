"""Autograding script for student homework."""

import os
import subprocess


def test_homework():
    """Test Word Count"""

    for path in [
        "Dockerfile",
        ".dockerignore",
    ]:
        if not os.path.exists(path):
            raise Exception(f"'{path}' directory does not exist")
