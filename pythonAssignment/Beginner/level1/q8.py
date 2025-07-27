"""8. Write a Python program to calculate the LCM (Least Common Multiple) of two numbers.
        number1 = 12, number2 = 18
        LCM of 12 and 18 are: 36
"""

def lcm(a, b):
    greater = max(a, b) # since, lcm can't be graeter than max number of the given numbers

    for i in range(greater, a * b + 1): # going till a*b + 1 sicne, lcm cant be graeter than product of their given numbers
        if i % a == 0 and i % b == 0:
            return i

print("LCM is:", lcm(12, 18))
