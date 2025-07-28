"""2. Write a program to count the lines in a file “demo.txt”
"""

def count_lines():
    with open("pythonAssignment\Beginner\level3\demo.txt") as f:
        data = f.read()
        lines = data.split('\n')
    return len(lines)

print(count_lines())
