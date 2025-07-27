"""8. Write a Python function that counts the number of vowels in a given string.
Sample Input: string = "Hello, World!"
Sample Output: Number of vowels: 3
"""

string = "Hello, World!"

def vowels_count(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count_vowels = {}
    for i in string.lower():
        if i in vowels:
            if i in count_vowels:
                count_vowels[i] += 1
            else:
                count_vowels[i] = 1
    return f"Number of vowels: {sum(count_vowels.values())}"


print(vowels_count(string))
