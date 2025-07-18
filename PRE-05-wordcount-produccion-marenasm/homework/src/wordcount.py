import sys

from ._internals.count_words import count_words
from ._internals.preprocess_lines import preprocess_lines
from ._internals.read_all_lines import read_all_lines
from ._internals.split_into_words import split_into_words
from ._internals.write_word_counts import write_word_counts


def main():
    """Main function to orchestrate the word count process."""

    if len(sys.argv) != 3:
        print("Usage: python3 -m homework <input_folder> <output_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    lines = read_all_lines(input_folder)
    preprocessed_lines = preprocess_lines(lines)
    words = split_into_words(preprocessed_lines)
    word_counts = count_words(words)
    write_word_counts(output_folder, word_counts)


if __name__ == "__main__":
    main()
