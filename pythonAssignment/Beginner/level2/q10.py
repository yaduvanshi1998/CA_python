"""10. We are making n stone piles! The first pile has n stones. 
        If n is even, then all piles have an even number of stones. 
        If n is odd, all piles have an odd number of stones. 
        Each pile must have more stones than the previous pile but as few as possible. 
        Write a Python program to find the number of stones in each pile.
        Sample Input: n = 7
        Sample Output: Stones in a single pile = [2, 4, 6]
"""

def stone_piles(n):
    piles = []
    count = n // 2  
    
    # If n is odd, piles have even stones starting from 2
    # If n is even, piles have odd stones starting from 1
    if n % 2 == 1:
        start = 2
    else:
        start = 1
    
    # Add piles with stones increasing by 2 each time
    for i in range(count):
        piles.append(start + 2 * i)
    
    return f"Stones in a single pile: {piles}"

n = 7
print(stone_piles(n))
