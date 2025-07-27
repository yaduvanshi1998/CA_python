"""7. Write a Python function that finds the median of a list of numbers.
        Sample Input: number_list = [7, 2, 5, 1, 9, 3]
        Sample Output: Median: 4.0
"""

number_list = [7, 2, 5, 1, 9, 3]

def find_median(lst):
    sorted_lst = sorted(lst)  
    n = len(sorted_lst)

    mid = n // 2

    if n % 2 == 0: # divisible by 2 and will have 0 as remainder (like 2,4,6,8,....)
        median = (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:           # not divisible by 2 like 3,5,7,9,.....
        median = sorted_lst[mid]

    return median

print(find_median(number_list))
