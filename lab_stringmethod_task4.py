'''4. Write a Python Count vowels in a string input= “Welcome to Python Assignment”

 Output: Total vowels are: 8'''
def count_vowels(input_string):
    # Define the set of vowels
    vowels = "aeiouAEIOU"
    
    # Initialize a counter for vowels
    vowel_count = 0
    
    # Iterate through each character in the string
    for char in input_string:
        if char in vowels:  # Check if the character is a vowel
            vowel_count += 1  # Increment the counter
    
    return vowel_count

# Input string
input_string = "Welcome to Python Assignment"

# Get the count of vowels
total_vowels = count_vowels(input_string)

# Print the result
print(f"Total vowels are: {total_vowels}")
