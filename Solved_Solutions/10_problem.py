"""
Project Euler Problem 10 - Summation of Primes

Answer: 142913828922
Elapsed time (seconds): 9.1130

Solved with Python 3.10.12
Author: dnicolauit
""" 
from math import sqrt
import time

max_prime = 2000000
def sum_primes(max_prime):
    count = 3
    solution = 2
    while True:
        isprime = True
        
        for x in range(2, int(sqrt(count) + 1)):
            if count % x == 0: 
                isprime = False
                break
        
        if isprime:
            if count < max_prime:
                solution += count
            else: 
                return solution
        
        count += 1

start_time = time.time()
solution = sum_primes(max_prime)
end_time = time.time()

elapsed_time = end_time - start_time
print("Solution: ", solution)
print("Elapsed time: ", elapsed_time) 


