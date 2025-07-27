"""2. Write a program that accepts a string as input from the user and calculates the number of digits and letters.
        Input: Hello123
        Output: Alphabets: 5 & Number : 3

"""

def count_string_and_int():
    string_input = input("enter the string with characters and numbers! \n")
    char_count = 0
    int_count = 0

    for j in string_input:
        if j.isalpha():
            char_count += 1
        elif j.isdigit():
            int_count += 1
        else:
            pass
    return f"count of characters in your string are {char_count} and integers are {int_count}"

print(count_string_and_int())

# if we dont want to use the inbuilt isaplha and isdigi method then we can use ord() method where we can check str and int by ascii values

# def count_string_and_int():
#     string_input = input("Enter the string with characters and numbers! \n")
#     char_count = 0
#     int_count = 0

#     for ch in string_input:
#         ascii_val = ord(ch)

#         if 48 <= ascii_val <= 57:
#             int_count += 1
#         elif (65 <= ascii_val <= 90) or (97 <= ascii_val <= 122):
#             char_count += 1
#         else:
#             pass

#     return f"count of characters in your string are {char_count} and integers are {int_count}"

# print(count_string_and_int())
