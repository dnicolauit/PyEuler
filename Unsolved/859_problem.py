"""
Project Euler Problem 859 - Cookie Game

Answer: 
Elapsed time (seconds): 

Solved with Python 3.10.12
Author: dnicolauit
""" 


N = 7

def first_even(piles):
    for i, pile in enumerate(piles):
        if pile % 2 == 0:
            return i

# Create a list of lists where each list contains the division of the number N into at list N
def divide_piles(N):
    piles = []


    
    return piles


# def game(): 


print(divide_piles(N))



# piles = [5,4,9,3,1,5]
# x = piles[first_even(piles)]
# print(x)