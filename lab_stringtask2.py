##Write a Python program to remove a newline in Python String = "\nBest \nDeeptech \nPython \nTraining\n"
# Given string with newlines
string = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove newlines using the replace() function
cleaned_string = string.replace("\n", " ")

# Print the result
print(cleaned_string.strip())
