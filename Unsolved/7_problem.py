"""
Project Euler Problem 7 - 10001st prime

Answer: 
Elapsed time (seconds): 

Solved with Python 3.10.12
Author: dnicolauit
""" 

from math import sqrt

def prime_factors(n):
    factors = []
    
    # Handle divisible by 2 separately 
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check odd factors
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    # If n is a prime number greater than 2, add it
    # Usually this number is 1
    if n > 2:
        factors.append(n)

    return factors

i=0
factors = []
while len(factors)<10001:
    factors.extend(x for x in prime_factors(i) if x not in factors)
    i+=1