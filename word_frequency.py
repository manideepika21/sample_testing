import re
from collections import Counter

def clean_text(text):
    """
    Remove non-alphanumeric characters and convert text to lowercase.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', text).lower()

def count_word_frequency(file_path):
    """
    Count the frequency of each word in the given file.
    """
    try:
        '''with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            cleaned_text = clean_text(text)
            words = cleaned_text.split()
            word_counts = Counter(words)'''

        return word_counts
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

def display_top_words(word_counts, top_n=10):
    """
    Display the top N most common words.
    """
    print(f"\nTop {top_n} most common words:")
    for word, count in word_counts.most_common(top_n):
        print(f"{word}: {count}")

if __name__ == "__main__":
    # Example usage
    file_path = input("Enter the path to your text file: ")
    word_counts = count_word_frequency(file_path)

    if word_counts:
        display_top_words(word_counts, top_n=10)
