"""10. Write a Python program to reverse the order of words in a given sentence.
        Input_sentence = “Hello, World! Welcome to Python
        programming.”
        Output after reverse = “programming. Python to Welcome
        World! Hello,”
"""

input_sentence = "Hello, World! Welcome to Python programming."

def reverse_sentence(input_sentence):
    splitted_data = input_sentence.split(' ')
    reversed_sentence = ""
    for i in range(len(splitted_data)-1, 0, -1):
        reversed_sentence += splitted_data[i]+ " "
    
    return reversed_sentence


print(reverse_sentence(input_sentence))
    