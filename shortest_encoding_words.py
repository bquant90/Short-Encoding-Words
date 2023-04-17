# This program finds the length of the shortest reference string that can encode an array of words.
# Criteria: - The reference string ends with '#'
# - For each word in the array, there is an index that specifies the starting position of the word in the reference string. The substring from that position up to the next '#' character is equal to the word.

def main():
  words = ["time", "me", "bell"]
  print(f"Words in the array: {words}")
  solution, length = shortest_ref_string(words)
  print(f"Shortest reference string: {solution}")
  print(f"Length of the shortest reference string: {length}\n")

  print("Let's try this again with another word array.")
  words_2 = ["skate", "short", "sentence", "range", "lecture"]
  print(f"Words in the array: {words_2}")
  solution_2, length_2 = shortest_ref_string(words_2)
  print(f"Shortest reference string: {solution_2}")
  print(f"Length of the shortest reference string: {length_2}")
  
def shortest_ref_string(words: list[str]) -> tuple[str, int]:
  word_set = set(words)
  word_indices = {word: i for i, word in enumerate(words)}  # Create a dictionary to store word indices.
  
  # The for loop eliminate words from the set that are suffixes (string of letters that go after a word, like pain-ful, where 'ful' is the suffix.) of other words in the words list, as they are not needed in the final reference string.
  for word in list(word_set):
    for i in range(1, len(word)):
      word_set.discard(word[i:])
            
  sorted_words = sorted(word_set, key=lambda word: word_indices[word])  # Get word indices from the dictionary.
  ans = f"{'#'.join(sorted_words)}#"
  return ans, len(ans)

main()
