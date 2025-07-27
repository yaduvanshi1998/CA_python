"""3. Write a Python program to input marks for five subjects Physics,
    Chemistry, Biology, Mathematics, and Computer. Calculate the
    percentage and grade according to the following:

    Percentage >= 90% : Grade A
    Percentage >= 80% : Grade B 
    Percentage >= 70% : Grade C
    Percentage >= 60% : Grade D
    Percentage >= 40% : Grade E
    Percentage < 40% : Grade F
"""

def percentage_calculator():
    physics = int(input("Enter the obtained physics marks out of 100: \n"))
    chemistry = int(input("Enter the obtained chemistry marks out of 100: \n"))
    biology = int(input("Enter the obtained biology marks out of 100: \n"))
    mathematics = int(input("Enter the obtained mathematics marks out 100: \n"))
    computer = int(input("Enter the obtained computer marks out of 100: \n"))

    total_marks = (physics + chemistry + biology + mathematics + computer)
    print("Total marks is:", total_marks)
    percentage = (total_marks/500)*100
    print("percentage:", percentage)

    ''' If you want to see the rounded percentage use below code

        rounded_percentage = round(percentage, 2)
        print("rounded percentage:", rounded_percentage)
    '''
   
    if percentage < 40:
        return "Grade F"
    elif percentage >= 40 and percentage < 60:
        return "Grade E"
    elif percentage >= 60 and percentage < 70:
        return "Grade D"
    elif percentage >= 70 and percentage < 80:
        return "Grade C"
    elif percentage >= 80 and percentage < 90:
        return "Grade B"
    elif percentage >= 90 and percentage < 100:
        return "Grade A"
    else:
        return "Error: Check the marks you entered!"
    
print(percentage_calculator())