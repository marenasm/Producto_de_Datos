def count_words(words):
    """Count occurrences of each word using a plain dictionary."""
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts
