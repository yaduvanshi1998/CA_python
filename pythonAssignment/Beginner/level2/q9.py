"""9. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range."""

def element_at_index(lst, i):
    try:
        print(f"Element at index {i} is: {lst[i]}")
    except IndexError:
        print(f"Error: Index {i} is out of range for the list.")

my_list = [10, 20, 30, 40, 50]

element_at_index(my_list, 2)

element_at_index(my_list, 10)
