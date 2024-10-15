'''2. Write a Python program to remove duplicate characters of a given string. 

Input = “String and String Function”

 Output: String and Function '''

def remove_duplicate_words(input_string):
    # Split the input string into words
    words = input_string.split()

    # Use a list to preserve the order and a set to track seen words
    result = []
    seen = set()

    for word in words:
        if word not in seen:
            result.append(word)  # Add to result if not seen
            seen.add(word)  # Mark word as seen
    
    # Join the list back into a string
    return ' '.join(result)

# Input string
input_string = "String and String Function"

# Get the output string with duplicate words removed
output_string = remove_duplicate_words(input_string)

# Print the result
print(f"Output: {output_string}")

