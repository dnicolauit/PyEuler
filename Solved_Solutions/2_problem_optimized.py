"""
Project Euler Problem 2 - Even Fibonacci Numbers

Answer: 4613732
Elapsed time (seconds): 4.2915e-06
Solved with Python 3.10.12
Author: nicoVascon
""" 

import time

limit = 4000000

def fibonacci(limit):
    a = 1
    b = 0
    n = 0
    x = 0
    while True:
        n = a + b
        if n > limit:
            return x
        b = a 
        a = n
        if n % 2 == 0:
            x = x + n


start_time = time.time()
even = fibonacci(limit)
end_time = time.time()

elapsed_time = end_time - start_time
print("Solution: ", even)
print("Elapsed time: ", elapsed_time) 