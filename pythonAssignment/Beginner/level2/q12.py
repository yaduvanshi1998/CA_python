"""12. Create a login page backend to ask users to enter the username and password. 
        Make sure to ask for a Re-Type Password and if the password is incorrect 
        give a chance to enter it again but it should not be more than 3 times.
"""

def login_page():
    username = input("Enter the username: \n")
    password = input("Enter the password: \n")

    for attempt in range(3):
        re_type_password = input("Re-enter the password: \n")
        if re_type_password == password:
            return "Login successful"
        else:
            print(f"Passwords do not match. Attempt {attempt + 1} of 3")

    return "Login failed"

print(login_page())
