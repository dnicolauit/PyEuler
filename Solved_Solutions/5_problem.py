"""
Project Euler Problem 5 - Smallest Multiple

Answer: 232792560
Elapsed time (seconds): 3.6955e-05

Solved with Python 3.10.12
Author: dnicolauit
""" 

import time
import math

def prime_factors(max):
    # Function based on functino in 3_problem.py
    factors = []
    
    # Handle divisible by 2 separately 
    while max % 2 == 0:
        factors.append(2)
        max //= 2
    
    # Check odd factors
    for i in range(3, int(math.sqrt(max)) + 1, 2):
        while max % i == 0:
            factors.append(i)
            max //= i

    # If n is a prime number greater than 2, add it
    # Usually this number is 1
    if max > 2:
        factors.append(max)

    # Count occurences
    counts = {}
    for num in factors:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts

start_time = time.time()
max = 20
factors_dict = {}
for i in range(1, max+1):
    factors = prime_factors(i)
    for key, value in factors.items():
        if key in factors_dict:
            if value > factors_dict[key]:
                factors_dict[key] = value
        else:
            factors_dict[key] = value

solution = 1
for key, value in factors_dict.items():
    solution *= key**value

end_time = time.time()

elapsed_time = end_time - start_time
print("Solution: ", solution)
print("Elapsed time: ", elapsed_time) 

print(solution)
