'''1. Write a Python program to Count all letters, digits, and special symbols from the given string Input = “P@#yn26at^&i5ve” 

Output: 

Chars = 8 

Digits = 2 

Symbol = 3 '''

def count_chars_digits_symbols(input_string):
    chars = 0
    digits = 0
    symbols = 0
    
    # Iterate through each character in the string
    for char in input_string:
        if char.isalpha():
            chars += 1  # Count letters
        elif char.isdigit():
            digits += 1  # Count digits
        else:
            symbols += 1  # Count special symbols
    
    return chars, digits, symbols

# Input string
input_string = "P@#yn26at^&i5ve"

# Get counts
chars, digits, symbols = count_chars_digits_symbols(input_string)

# Print results
print(f"Chars = {chars}")
print(f"Digits = {digits}")
print(f"Symbols = {symbols}")
