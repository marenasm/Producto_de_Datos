import os


def read_all_lines(input_folder):
    """Read all lines from all files in the input folder."""

    lines = []
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            lines.extend(f.readlines())
    return lines
