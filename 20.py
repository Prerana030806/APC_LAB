import string
from collections import Counter

def word_count(file_path):
    # Open and read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Convert to lowercase and remove punctuation
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Split into words
    words = text.split()
    
    # Count total words
    total_words = len(words)
    print(f"Total number of words: {total_words}")
    
    # Count frequency of each word
    word_freq = Counter(words)
    
    # Display top 10 most frequent words
    print("\nTop 10 most frequent words:")
    for word, freq in word_freq.most_common(10):
        print(f"{word}: {freq}")
word_count("sample.txt")
word_count("sample.txt")

# Example usage