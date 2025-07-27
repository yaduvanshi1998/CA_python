"""9. Write a Python program to count the frequency of each element in a list.
        Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
        Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}
"""

input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]

def freq_count(input_list):
    count_num = {}
    for i in  input_list:
        if i not in count_num:
            count_num[i] = 1
        else:
            count_num[i] += 1
    return count_num

print(freq_count(input_list))