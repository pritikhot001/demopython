###Write a Python program to count and display the vowels of a given text String=”Welcome to python Training

# Given string
string = "Welcome to python Training"

# Convert the string to lowercase for easy comparison
string = string.lower()

# Define the vowels
vowels = "aeiou"

# Initialize a counter and a list to store the vowels found
vowel_count = 0
vowels_found = []

# Loop through each character in the string
for char in string:
    if char in vowels:
        vowel_count += 1
        vowels_found.append(char)

# Display the number of vowels and the vowels themselves
print(f"Number of vowels: {vowel_count}")
print(f"Vowels found: {' '.join(vowels_found)}")
