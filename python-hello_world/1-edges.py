#!/usr/bin/python3

word = "Holberton"

# Extract the first 3 letters of the variable "word"
word_first_3 = word[:3]

# Extract the last 2 letters of the variable "word"
word_last_2 = word[-2:]

# Extract the middle word without the first and last letters
middle_word = word[1:-1]

print("First 3 letters:", word_first_3)
print("Last 2 letters:", word_last_2)
print("Middle word:", middle_word)
