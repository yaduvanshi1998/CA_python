"""8. You need to write a function that accepts an encoded string as a parameter.
    This string will contain a first name, last name, and an id.
    Values in the string can be separated by any number of zeros. 
    The id is a numeric value but will contain no zeros. 
    The function should parse the string and return a Python dictionary that contains the first name, last name, and id values.
    For example:
    Input : “Robert000Smith000123”
    Output:
    { “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }
"""

import re

def parse_encoded_string_regex(s):
    # Split the string on one or more zeros (0+)
    parts = re.split(r'0+', s)

    if len(parts) != 3:
        raise ValueError("Input string does not contain exactly three parts separated by zeros.")
    
    return {
        "first_name": parts[0],
        "last_name": parts[1],
        "id": parts[2]
    }

input_str = "Robert000Smith000123"
print(parse_encoded_string_regex(input_str))
