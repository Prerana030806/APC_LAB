def find_long_words(sentence, k):
  words = sentence.split()  # Split the sentence into a list of words
  long_words = []
  for word in words:
    if len(word) > k:
      long_words.append(word)
  return long_words

# Example usage:
input_sentence = "This is a sample sentence with some long words."
min_length = 4
result = find_long_words(input_sentence, min_length)
print(f"Words longer than {min_length} in '{input_sentence}': {result}")