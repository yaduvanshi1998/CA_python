"""4. Given an array of size N. The task is to rotate array by D elements towards right
Sample Input: arr = [1, 2, 3, 4, 5], D = 2
Sample Output: arr after rotation = [4, 5, 1, 2, 3]
"""

arr = [1, 2, 3, 4, 5]
d = 2

def rotate_list(arr, d):
    n = len(arr)
    for i in range(d):
        last = arr[-1]
        for j in range(n - 1, 0, -1):
            arr[j] = arr[j - 1]
        arr[0] = last
    return arr

print(rotate_list(arr, d))