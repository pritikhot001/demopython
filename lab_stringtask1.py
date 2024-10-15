#Write a Python program to count the occurrences of each word in a given sentence string = “To change the overall look of your document. To change the look available in the gallery”
# Given sentence
sentence = "To change the overall look of your document. To change the look available in the gallery"

# Convert the sentence to lowercase and split it into words
words = sentence.lower().replace('.', '').split()

# Create an empty dictionary to store word counts
word_count = {}

# Count the occurrences of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the word occurrences
for word, count in word_count.items():
    print(f"'{word}': {count}")
