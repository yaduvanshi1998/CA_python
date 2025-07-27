"""5. Write a Python program to find the factorial of a number using a for loop.
"""

def factorial():
    num = int(input("Enter the number you want factorial of: \n"))
    f = 1
    for i in range(1, num+1):
        f *= i
    return f"Factorial of {num} is {f}"

print(factorial())