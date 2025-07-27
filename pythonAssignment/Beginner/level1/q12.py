"""12. Write a Python program to reverse a number using a while loop.
    Sample Input: num = 12345
    Sample Output: revnum = 54321
"""

def reverse_num():
    num = 12345
    num_list = list(str(num))
    l = 0
    r = len(num_list) - 1
    while l < r:
        temp = num_list[l]
        num_list[l] = num_list[r]
        num_list[r] = temp
        l += 1
        r -= 1
    return ''.join(num_list)

print(reverse_num())

    