"""3. Aditi has used text editing software to type some text. 
    After saving the article as words.txt, she realized that she had wrongly
    typed the alphabet “J" instead of “I" everywhere in the article.
    Write a function definition for JtoI() in Python 
    that would display the corrected version of the entire content of the file WORDS.TXT
    with all the alphabet "J" to be displayed as an alphabet "I" on the screen.

    Note: Assume that words.txt does not contain any J alphabet
    otherwise.
"""

def j_to_i():
    with open("pythonAssignment/Beginner/level3/words.txt", "r") as f:
        data = f.read()
        
    if 'J' in data:
        return data.replace('J', 'I')
    else:
        return "There is no 'J' letter in your words.txt file."

print(j_to_i())
