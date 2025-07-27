"""1. Write a Python program to find the common elements between two lists.
        Sample Input: l1 = [1, 2, 3, 4, 5] and l2 = [4, 5, 6, 7, 8]
        Sample output: [4, 5]
"""
l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]

def common_elements():
    common_nums = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                common_nums.append(l2[j])
    return common_nums

print(common_elements())

# to avoid using nested loop, this can be also solved with the following

def common_elements():
    common_nums = []
    for num in l1:
        if num in l2:
            common_nums.append(num)
    return common_nums

print(common_elements())