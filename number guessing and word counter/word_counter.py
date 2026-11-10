"""
Word Counter
A tool to count words, characters, lines, and other statistics in text.
"""

import re
import sys
from collections import Counter


def count_words(text):
    """Count words in text."""
    words = re.findall(r'\b\w+\b', text.lower())
    return len(words), words


def count_characters(text, include_spaces=True):
    """Count characters in text."""
    if include_spaces:
        return len(text)
    return len(text.replace(' ', '').replace('\n', '').replace('\t', ''))


def count_lines(text):
    """Count lines in text."""
    if not text:
        return 0
    return text.count('\n') + 1


def count_sentences(text):
    """Count sentences in text."""
    # Simple sentence counting based on punctuation
    sentences = re.split(r'[.!?]+', text)
    return len([s for s in sentences if s.strip()])


def count_paragraphs(text):
    """Count paragraphs in text."""
    paragraphs = text.split('\n\n')
    return len([p for p in paragraphs if p.strip()])


def get_word_frequency(words, top_n=10):
    """Get most frequent words."""
    word_counts = Counter(words)
    return word_counts.most_common(top_n)


def get_character_frequency(text, top_n=10):
    """Get most frequent characters."""
    # Only count alphabetic characters
    chars = [c.lower() for c in text if c.isalpha()]
    char_counts = Counter(chars)
    return char_counts.most_common(top_n)


def analyze_text(text):
    """Perform complete text analysis."""
    if not text.strip():
        return None

    word_count, words = count_words(text)
    char_count_with_spaces = count_characters(text, True)
    char_count_without_spaces = count_characters(text, False)
    line_count = count_lines(text)
    sentence_count = count_sentences(text)
    paragraph_count = count_paragraphs(text)

    # Calculate averages
    avg_words_per_sentence = word_count / sentence_count if sentence_count > 0 else 0
    avg_chars_per_word = char_count_without_spaces / word_count if word_count > 0 else 0

    # Get frequency data
    top_words = get_word_frequency(words, 10)
    top_chars = get_character_frequency(text, 10)

    return {
        'word_count': word_count,
        'char_count_with_spaces': char_count_with_spaces,
        'char_count_without_spaces': char_count_without_spaces,
        'line_count': line_count,
        'sentence_count': sentence_count,
        'paragraph_count': paragraph_count,
        'avg_words_per_sentence': avg_words_per_sentence,
        'avg_chars_per_word': avg_chars_per_word,
        'top_words': top_words,
        'top_chars': top_chars
    }


def print_results(stats):
    """Print analysis results in a formatted way."""
    if not stats:
        print("No text to analyze.")
        return

    print("\n" + "=" * 50)
    print("           TEXT ANALYSIS RESULTS")
    print("=" * 50)

    print(f"\n[+] Basic Statistics:")
    print(f"   Words:           {stats['word_count']:,}")
    print(f"   Characters:      {stats['char_count_with_spaces']:,} (with spaces)")
    print(f"   Characters:      {stats['char_count_without_spaces']:,} (without spaces)")
    print(f"   Lines:           {stats['line_count']:,}")
    print(f"   Sentences:       {stats['sentence_count']:,}")
    print(f"   Paragraphs:      {stats['paragraph_count']:,}")

    print(f"\n[+] Averages:")
    print(f"   Words/Sentence:  {stats['avg_words_per_sentence']:.1f}")
    print(f"   Chars/Word:      {stats['avg_chars_per_word']:.1f}")

    print(f"\n[+] Top 10 Most Frequent Words:")
    for i, (word, count) in enumerate(stats['top_words'], 1):
        print(f"   {i:2d}. {word:<15} ({count})")

    print(f"\n[+] Top 10 Most Frequent Characters:")
    for i, (char, count) in enumerate(stats['top_chars'], 1):
        print(f"   {i:2d}. '{char}' ({count})")

    print("=" * 50)


def get_text_from_file(filepath):
    """Read text from a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def main():
    """Main program loop."""
    print("=" * 50)
    print("           WORD COUNTER")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("1. Analyze text from input")
        print("2. Analyze text from file")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ").strip()

        if choice == '1':
            print("\nEnter your text (press Enter twice to finish):")
            lines = []
            empty_count = 0
            while empty_count < 2:
                line = input()
                if line == '':
                    empty_count += 1
                else:
                    empty_count = 0
                lines.append(line)
            text = '\n'.join(lines[:-1])  # Remove last empty line

            if text.strip():
                stats = analyze_text(text)
                print_results(stats)

        elif choice == '2':
            filepath = input("Enter file path: ").strip()
            text = get_text_from_file(filepath)
            if text is not None:
                stats = analyze_text(text)
                print_results(stats)

        elif choice == '3':
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()