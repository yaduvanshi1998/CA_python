"""9. Given an input string, write a function that returns the run length encoded string for the input string.
    For Example:
    Input: wwwwaaadebbbbbw
    Output: w4a3d1e1b5w1
"""

def run_length_encode(s):
    if not s:
        return ""
    
    encoded = ""
    count = 1
    
    for i in range(len(s)):
        # If next char is same, increase count
        if i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
        else:
            # Otherwise, append current char and count, reset count
            encoded += s[i] + str(count)
            count = 1
    
    return encoded


input_str = "wwwwaaadebbbbbw"
print(run_length_encode(input_str))  
