def split_into_words(lines):
    """Split lines into individual words and clean punctuation."""
    words = []
    for line in lines:
        words.extend(word.strip(",.!?") for word in line.split())
    return words
