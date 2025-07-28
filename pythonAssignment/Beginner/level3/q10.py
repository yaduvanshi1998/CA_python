"""10. A cafe has N computers. Several customers come to the cafe to use these computers. 
    A customer will be serviced only if there is any unoccupied computer at the moment the customer visits the cafe. 
    If there is no unoccupied computer, the customer leaves the cafe.
    You are given an integer N representing the number of computers in the cafe and a sequence of uppercase letters S. 
    Every letter in S occurs exactly two times. 
    The first occurrence denotes the arrival of a customer and the second occurrence denotes the departure of the same customer
    if he gets allocated the computer.
    You have to find the number of customers that walked away without using a computer.
    Example 1:
    Input:
    N = 3
    S = GACCBDDBAGEE
    Output: 1
    Explanation: Only D will not be able to get any computer. So the
    answer is 1.
    Example 2:
    Input:
    N = 1
    S = ABCBAC
    Output: 2
    Explanation: B and C will not be able to get any computers. So the
    answer is 2.
"""

def count_walk_aways(N, S):
    occupied = set()
    in_cafe = set()
    walk_aways = 0
    available = N

    for c in S:
        if c not in in_cafe:
            in_cafe.add(c)
            if available > 0:
                occupied.add(c)
                available -= 1
            else:
                walk_aways += 1
        else:
            in_cafe.remove(c)
            if c in occupied:
                occupied.remove(c)
                available += 1

    return walk_aways

print(count_walk_aways(3, "GACCBDDBAGEE"))  
print(count_walk_aways(1, "ABCBAC"))       
