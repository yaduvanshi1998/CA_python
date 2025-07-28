"""7. Write a program to construct a dictionary from the two lists containing the names of students
        and their corresponding subjects. 
        The dictionary should map the students with their respective subjects. 
        Let’s see how to do this using for loops and dictionary comprehension.
        Input: [Sam, Alice, Mona] ,
        [Commerce, Science, Computer]
        Output: [Sam: Commerce, Alice: Science , Mona: Computer]
"""

input1 = ['Sam', 'Alice', 'Mona'] 
input2 = ['Commerce', 'Science', 'Computer']


student_subject_dict = {}

for i in range(len(input1)):
    student_subject_dict[input1[i]] = input2[i]

print(student_subject_dict)
