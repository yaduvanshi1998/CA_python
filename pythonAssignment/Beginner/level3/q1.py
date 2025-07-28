"""1.Read the doc.txt file using Python File handling concept and return only the even length string
    from the file. Consider the content of doc.txt as given below:
    Hello I am a file
    Where you need to return the data string which is of even length.
    Make sure you return the content in The same link as it is present.
"""


def read_file():
    with open("pythonAssignment/Beginner/level3/doc.txt") as f:
        for line in f:
            words = line.split()
            for word in words:
                if len(word) % 2 == 0:
                    print(word, end=' ')
            print() 

read_file()

