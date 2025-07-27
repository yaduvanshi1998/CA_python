"""6. Write a Python program to check if a number is a power of two using recursion.
"""

def is_power_of_two(n):
    if n == 1:
        return True
    if n == 0 or n % 2 != 0:
        return False
    return is_power_of_two(n // 2)

n = int(input("Enter the number you want to check if it's a power of 2: \n"))

if is_power_of_two(n):
    print(f"{n} is a power of two.")
else:
    print(f"{n} is not a power of two.")
