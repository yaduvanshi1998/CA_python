"""4. Write a Python program to find the sum of all odd numbers between two given numbers.
        Start = 1, stop = 10
        Sum of odd numbers: 25

"""

def sum_of_odd_nums():
    sum_off_odd_num = 0
    for i in range(1,11):
        if i % 2 != 0:
            sum_off_odd_num += i
    return f"sum of all the odd numbers from '1-10' is {sum_off_odd_num}"

print(sum_of_odd_nums())


# If you want to get the user input for start and stop the use the below code

"""
    def sum_of_odd_nums():
    start = int(input("Enter the start number: \n"))
    stop = int(input("Enter the stop number: \n"))

    sum_of_odd_num = 0
    for num in range(start, stop + 1):
        if num % 2 != 0:
            sum_of_odd_num += num

    return f"Sum of all odd numbers between {start} and {stop} is {sum_of_odd_num}"

print(sum_of_odd_nums())
"""


