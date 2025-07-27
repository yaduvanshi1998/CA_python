"""Write a Python program to check if a given number is a perfect number.
    A Perfect number is a positive integer that is equal to the sum of its proper divisors. 
    For instance, 6 has divisors 1, 2, and 3, and 1 + 2 +
    3 = 6, so 6 is a perfect number.
    Input: 5
    Output: No
"""

def perfect_num():
    num = int(input("Enter the number you want to see if it's a perfect number! \n"))
    sum_of_divisor = 0
    if num < 2:
        return False
    
    for i in range(1, num):
        print(i)
        if num % i == 0:
            sum_of_divisor += i
    if sum_of_divisor == num:
        return True
    else:
        return False
        
print(perfect_num())
