"""13. Write a Python program to find if a given string starts with a given character using Lambda.
        Sample input: input_string = "Hello, World!", given_char = "H"
        Sample Output: True
"""

input_string = "Hello, World!"
given_char = "H"

starts_with_char = lambda input_string, given_char: input_string.startswith(given_char)

print(starts_with_char(input_string, given_char))
