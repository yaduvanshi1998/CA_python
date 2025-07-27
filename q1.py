"""1. Write a program in Python to perform the following operation:

        -> If a number is divisible by 3 it should print “Consultadd” as a
            string
        -> If a number is divisible by 5 it should print “Python Training” as
            a string
        -> If a number is divisible by both 3 and 5 it should print
            “Consultadd - Python Training” as a string.
"""

def print_string(): 
    num = int(input("enter number to see the string! \n"))
    if num % 3 == 0 and num % 5 == 0: # had to mention this condition first, 
        # since other conditions were getting true and the execution was not to reaching this condition 
        # for number like 15
        return "Consultadd - Python Training"
    elif num % 3 == 0:
        return "Consultadd"
    elif num % 5 == 0:
        return "Python Training"
    else:
        return "Neither divisible by 3 nor 5"  
    
print(print_string())
