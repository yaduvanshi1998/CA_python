"""11. Write a Python program to calculate the sum of digits of a given number until the sum becomes a single-digit number.
        Sample Input: num = 987
        Sample Output: Sum_of_digits = 24,
        Again compute the sum of digits so that it can be reduced to
        on single digit.
        Final Output: 6
"""

def sum_till_single_digit():
    num = int(input("Enter the number you want the sum of: \n"))

    while num > 9:
        summation = 0

        for digit in str(num):
            summation += int(digit)
        num = summation
        
    return summation

print("Final Output:", sum_till_single_digit())
