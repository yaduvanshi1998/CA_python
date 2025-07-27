"""3. Given an array of N integers and an integer K, find the number of pairs of elements in the array whose sum is equal to K.
        Sample Input: arr = [1, 2, 3, 4, 5], k = 6
        Sample Output: Pair count: 2
"""
arr = [1, 2, 3, 4, 5]
k = 6

def elements_pair(arr, k):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == k:
                count += 1
    return f"Pair count: {count}"

print(elements_pair(arr, k))