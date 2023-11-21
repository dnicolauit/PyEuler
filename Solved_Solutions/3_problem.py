"""
Project Euler Problem 3 - Largest prime factor

Answer: 6857
Elapsed time (seconds): 0.0153

Solved with Python 3.10.12
Author: dnicolauit
"""

import time
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



number  = 600851475143

start_time = time.time()
x = max(prime_factors(number))
end_time = time.time()

elapsed_time = end_time - start_time
print("Solution: ", x)
print("Elapsed time: ", elapsed_time) 
