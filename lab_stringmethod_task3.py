'''3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN” 

Output: 

UpperCase : 5 

LowerCase : 18 

NumberCase : 5 

SpecialCase : 11 '''

def count_characters(input_string):
    upper_case = 0
    lower_case = 0
    number_case = 0
    special_case = 0

    # Iterate through each character in the string
    for char in input_string:
        if char.isupper():
            upper_case += 1  # Count uppercase letters
        elif char.islower():
            lower_case += 1  # Count lowercase letters
        elif char.isdigit():
            number_case += 1  # Count numeric values
        else:
            special_case += 1  # Count special characters

    return upper_case, lower_case, number_case, special_case

# Input string
input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"

# Get the counts
upper_case, lower_case, number_case, special_case = count_characters(input_string)

# Print the results
print(f"UpperCase : {upper_case}")
print(f"LowerCase : {lower_case}")
print(f"NumberCase : {number_case}")
print(f"SpecialCase : {special_case}")
