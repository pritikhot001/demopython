##Write a Python program to reverse words in a string String = “Deeptech Python Training” 

# Given string
string = "Deeptech Python Training"

# Split the string into words, reverse the list of words, and join them back into a string
reversed_words = ' '.join(string.split()[::-1])

# Print the result
print(reversed_words)
