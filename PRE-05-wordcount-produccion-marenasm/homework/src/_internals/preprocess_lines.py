def preprocess_lines(lines):
    """Preprocess lines by normalizing and cleaning text."""
    return [line.lower().strip() for line in lines]
