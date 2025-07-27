"""7. Write a Python program to check if a string is an anagram of another string.
string1 = "listen", string2 = "silent"
Output: True
"""

string1 = "lzzten"
string2 = "zzlent"
def anagram(string1, string2):
    count_string1 = {}
    count_string2 = {}

    if len(string1) != len(string2):
        return False
    
    for i in string1:
        if i not in count_string1:
            count_string1[i] = 1
        else:
            count_string1[i] += 1

    for j in string2:
        if j not in count_string2:
            count_string2[j] = 1
        else:
            count_string2[j] += 1

    for ch in count_string1:
        # print(ch)
        # print("count_string1:", count_string1[ch])
        # print("count_string2:", count_string2[ch])
        if count_string1[ch] != count_string2.get(ch, 0):
            return False
    return True


print(anagram(string1, string2))